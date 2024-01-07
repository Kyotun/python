import requests
import os
import datetime as dt
from requests.auth import HTTPBasicAuth

class WorkoutTracker():
    def __init__(self) -> None:
        self.gender:str = ""
        self.height:int = 0
        self.weight:int = 0
        self.age:int = 0
        
        self.headers:str= {"Authorization": "", 
                           "x-app-id": "", 
                           "x-app-key": "", 
                           "content-type": "application/json"}
        self.exercise_endpoint:str = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.sheet_endpoint:str = ""
        
        self.physical_properties()
        self.account_infos()
        
        
    def physical_properties(self) -> None:
        """Asks user to his/hers phsical properties for accurate evaluation.
        """
        self.gender = input("Please enter your gender: ")
        self.weight = input("Please enter your weight in kg: ")
        self.height = input("Please enter your height in cm: ")
        self.age = input("Please enter your age: ")
    
    
    def account_infos(self) -> None:
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
        
        self.sheet_endpoint = input("Please give the URL of the sheet endpoint from sheety.")
        sheet_name = input("Please enter the sheetname:")
        exercise = input("Which exercise(s) did you do?:")
        json_data = self.get_exercise_properties(exercise=exercise)

        for exercise in json_data["exercises"]:
            sheet_inputs = {
                sheet_name : {
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
        
        
    def set_sheet_url(self, url:str) -> None:
        """Assigns the given url as new endpoint of sheet.

        Args:
            url (str): Url of the sheet from sheety app.
        """
        self.sheet_endpoint = url
    
    
    def set_exercise_endpoint(self, url:str) -> None:
        """Assigns the given url as new endpoint of exercises.

        Args:
            url (str): Url of the exercises(eg. url from nutritionix app)
        """
        self.exercise_endpoint = url