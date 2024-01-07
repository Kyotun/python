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
        self.name:str = ""
        
        self.email:str = ""
        self.headers:str= {"x-app-id": "", "x-app-key": "", "content-type": "application/json"}
        self.exercise_endpoint:str = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.sheet_endpoint:str = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/workouts/tabellenblatt1"
        
        self.physical_properties()
        self.account_infos()
        
        
    def physical_properties(self) -> None:
        self.name = input("Please enter your name(eg. Alex Mustermann): ")
        self.gender = input("Please enter your gender: ")
        self.weight = input("Please enter your weight in kg: ")
        self.height = input("Please enter your height in cm: ")
        self.age = input("Please enter your age: ")
    
    
    def account_infos(self) -> None:
        self.email = input("Please enter your email: ")
        self.headers["x-app-id"] = input("Please enter your Nutritionix APP ID: ")
        self.headers["x-app-key"] = input("Please enter your Nutritionix APP Key: ")
    
    
    def add_exercise(self) -> None:
        date_today = dt.datetime.now().strftime("%d/%m/%Y")
        time_now = dt.datetime.now().strftime("%X")
        # self.sheet_endpoint = input("Please give the URL of the sheet endpoint from sheety.")
        # sheet_name = input("Please enter the sheetname:")
        exercise = input("Which exercise(s) did you do?:")
        json_data = self.get_exercise_properties(exercise=exercise)

        for exercise in json_data["exercises"]:
            sheet_inputs = {
                "tabellenblatt1": {
                    "date": date_today,
                    "time": time_now,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }
            sheet_response = requests.post(url=self.sheet_endpoint, json=sheet_inputs)
            
            
    def get_exercise_properties(self, exercise:str) -> dict:
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
        self.sheet_url = url
    
    
    def set_exercise_endpoint(self, url:str) -> None:
        self.exercise_endpoint = url