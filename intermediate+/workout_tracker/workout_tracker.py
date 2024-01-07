import requests
import os
import datetime as dt
from requests.auth import HTTPBasicAuth

APP_ID = os.environ.get("APP_ID_NUTRI")
APP_KEY = os.environ.get("APP_KEY_NUTRI")
AUTH_KEY_BEARER = os.environ.get("APP_AUTH_NUTRI")

class WorkoutTracker():
    def __init__(self) -> None:
        self.gender:str = ""
        self.height:int = 0
        self.weight:int = 0
        self.age:int = 0
        
        self.headers:str= {"Authorization": AUTH_KEY_BEARER, 
                           "x-app-id": APP_ID, 
                           "x-app-key": APP_KEY, 
                           "content-type": "application/json"}
        self.exercise_endpoint:str = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.sheet_endpoint:str = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/workouts/tabellenblatt1"
        self.sheet_name:str = ""
        
        self.set_physical_properties()
        self.set_account_infos()
        
        
    def set_physical_properties(self) -> None:
        """Asks user to his/hers phsical properties for accurate evaluation.
        """
        self.gender = input("Please enter your gender: ")
        self.weight = input("Please enter your weight in kg: ")
        self.height = input("Please enter your height in cm: ")
        self.age = input("Please enter your age: ")
    
    
    def set_account_infos(self) -> None:
        """Asks user to the APP ID, APP Key if there is.
        Lastly it asks the auth token, if there is a authentication method and sets these given variables
        as self variables.
        """
        self.headers["x-app-id"] = input("Please enter your Nutritionix APP ID(Press just enter if there is no.): ")
        self.headers["x-app-key"] = input("Please enter your Nutritionix APP Key(Press just enter if there is no.): ")
        if(input("Is there a auth method? 'y' or 'n': ") == 'y'):
            self.headers["Authorization"] = input("Please enter the token(in format -> Basic/Bearer TOKEN): ")
    
    
    def add_exercise(self) -> None:
        """Asks user for the url and sheet name, then adds date, time, exercise etc. to the sheet for
        each exercises.
        """
        date_today = dt.datetime.now().strftime("%d/%m/%Y")
        time_now = dt.datetime.now().strftime("%X")
        
        if self.sheet_endpoint == "":
            self.sheet_endpoint = input("Please give the URL of the sheet endpoint from sheety.")
        if self.sheet_name == "":
            self.sheet_name = input("Please enter the sheetname:")
        exercise = input("Which exercise(s) did you do?:")
        json_data = self.get_exercise_properties(exercise=exercise)

        for exercise in json_data["exercises"]:
            sheet_inputs = {
                self.sheet_name : {
                    "date": date_today,
                    "time": time_now,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }
            sheet_response = requests.post(url=self.sheet_endpoint, json=sheet_inputs, headers=self.headers)
            
            
    def get_exercise_properties(self, exercise:str) -> dict:
        """Takes exercise in format of natural language. Give it to the predefined website for evaluation.
        Takes the evaluations from the website and returns it as in json data format.

        Args:
            exercise (str): Exercise in natural language format.

        Returns:
            dict: Json data of the exercises. Contains calories, duration etc.
        """
        parameters = {
            "query": exercise,
            "age": self.age,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height
        }
        response = requests.post(url=self.exercise_endpoint, json=parameters, headers=self.headers)
        json_data = response.json()
        return json_data
        
        
    def get_rows(self) -> None:
        """Prints the rows of the target google sheet.
        If sheet name is not pre-defined, asks user for sheet name.
        """
        response = requests.get(url=self.sheet_endpoint, headers=self.headers)
        if self.sheet_name == "":
            self.sheet_name = input("Please enter the sheet name from sheety:")
        rows = response.json()[self.sheet_name]
        for row in rows:
            print(f"Date: {row['date']}, exercise: {row['exercise']}, calorie: {row['calories']}")
    
    
    def set_sheet_url(self, url:str) -> None:
        """Assigns the given url as new endpoint of sheet.

        Args:
            url (str): Url of the sheet from sheety app.
        """
        self.sheet_endpoint = url
    
    def set_sheet_name(self, sheet_name:str) -> None:
        """Changes the currently available sheet name with the given one.

        Args:
            sheet_name (str): String that contains the new sheet name, that will be changed with the old sheet name.
        """
        self.sheet_name = sheet_name