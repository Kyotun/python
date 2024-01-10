import requests
import os
import datetime as dt
from tracker_exception import TrackerException
import validators

APP_ID = os.environ.get("APP_ID_NUTRI")
APP_KEY = os.environ.get("APP_KEY_NUTRI")
AUTH_KEY_BEARER = os.environ.get("APP_AUTH_NUTRI")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/workouts/tabellenblatt1"

class WorkoutTracker():
    """Tracker of workouts.
    Takes the exercise informations from website Nutritionix and saves the entries with help of the website Sheety to the given google sheet.
    In the beginning, personal properties and account informations should be given.
    """
    def __init__(self) -> None:
        self.gender:str = ""
        self.height:int = 0
        self.weight:int = 0
        self.age:int = 0
        
        self.header_sheet:str={
            "Authorization": "",
        }
        self.header_exercise:str= {
            "x-app-id": "", 
            "x-app-key": "",
             }
        self.exercise_endpoint:str = EXERCISE_ENDPOINT
        self.sheet_endpoint:str = ""
        self.sheet_name:str = ""
        
    def add_exercise(self, exercise:str) -> None:
        """Checks the endpoints and sheet name first then give the exercise(text from user in natural language)
        to the webiste Nutritionix. Gets the evaluated informations from the website in list format.
        Exercise list contains informations like calories burned, duration in min etc. for every exercise.
        This function enters these information to the given google sheet url in form of columns.
        Columns should be pre exist in google sheet.
        Columns are -> 'date', 'time', 'exercise', 'duration', 'calories'.
        
        Args:
            exercise (str): Descriptopn of exercises in natural english language that user did.
        """
        self.check_endpoints()
        self.check_sheet_name(sheet_name=self.sheet_name, input_message="Please enter the sheet name: ")
        exercise_list = self.get_exercise_properties(exercise=exercise)
        
        date_today = dt.datetime.now().strftime("%d/%m/%Y")
        time_now = dt.datetime.now().strftime("%X")
        for exercise in exercise_list:
            sheet_inputs = {
                self.sheet_name : {
                    "date": date_today,
                    "time": time_now,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }
            sheet_response = requests.post(url=self.sheet_endpoint, json=sheet_inputs, headers=self.header_sheet)
            sheet_exception_message = "Error by getting response from sheet. Please check the auth token and/or connection beetween website Sheety and to your google sheet."
            self.check_response(response_code=sheet_response.status_code, exception_message=sheet_exception_message)
            print(f"Sheet response text: {sheet_response.text}, sheet response json: {sheet_response.json()}, sheet response status code: {sheet_response.status_code}")
    
    # CHECKERS
    def check_special_keys(self, special_key:str, exception_message:str) -> TrackerException or str:
        """Checks the given key. If its length <= 0, raises a Tracker Exception.

        Args:
            special_key (str): ID/Key or Auth token from website Sheety.
            ID and Key belongs to the account, auth token belongs to the specific sheet.
            exception_message (str): If length of special key is equal to 0 or smaller, this message to be shown.

        Returns:
            TrackerException: Tracker Exception, for to show the reason to user.
            str: Given special key(ID, key or auth token).
        """
        if len(special_key) <= 0:
            raise TrackerException(message=exception_message)
        return special_key
    
    def check_endpoints(self):
        """Checks the URL of the exercise and sheet endpoints with help of check_url function.
        """
        exercise_endpoint_message = "Please give the URL of the exercise endpoint from website Nutritionix: "
        sheet_endpoint_message = "Please give the URL of the sheet endpoint from website Sheety: "
        self.sheet_endpoint = self.check_url(url=self.sheet_endpoint, input_message=sheet_endpoint_message)
        self.exercise_endpoint = self.check_url(url=self.exercise_endpoint, input_message=exercise_endpoint_message)
    
    def check_response(self, response_code:str, exception_message:str = "Error by getting successfull response from website."):
        if response_code != 200:
            raise TrackerException(message=exception_message)
        
    def check_url(self, url:str, input_message:str = "Given URL is empty, please give a valid URL: ") -> Exception or str:
        """If the given URL has the response 200, url will be returned. Otherwise an exception will be raised.
        If URL is empty string, it will be asked to user.
        """
        if url == "":
            url = input(input_message)
        if not validators.url(url):
            raise TrackerException(message=f"{url} is not valid.")
        return url
    
    def check_sheet_name(self, sheet_name:str, input_message:str = "Please enter the sheet name: ") -> str:
        """If sheet name is empty, asks user for it.
        Sheet name from user and sheet name at the end of the sheet url should match.
        If they're not matching, an exception will be raised.
        """
        sheet_name_from_sheet_endpoint = self.sheet_endpoint.split("/")[-1]
        if sheet_name == "":
            sheet_name = input(input_message)
        if sheet_name != sheet_name_from_sheet_endpoint:
            raise TrackerException(message=f"Given sheet name {sheet_name} doesn't match with sheet name of sheet endpoint url {sheet_name_from_sheet_endpoint}.")
        return sheet_name
            
    def check_exercise_data(self, exercise_list:str) -> Exception or str:
        if len(exercise_list) == 0:
            raise TrackerException(message="There is no matching exercise data. Please try to write your exercise entry again.")
        return exercise_list
        
        
    def check_weight(self, weight:int) -> int or Exception:
        if weight < 0 or weight > 200:
            raise TrackerException(message="Weight should be between 0-200")
        return weight
    
    def check_gender(self, gender:str) -> str or Exception:
        if gender != "male" and gender != "female":
            raise TrackerException(message="Two genders only. Male and female.")
        return gender
    
    def check_height(self, height:int) -> int or Exception:
        if height < 50 or height > 300:
            raise TrackerException(message="Height should be between 50-300.")
        return height
    
    def check_age(self, age:int) -> int or Exception:
        if age < 0 or age > 120:
            raise TrackerException(message="Age should be between 0-120.")
        return age
            
    # GETTERS
    def get_exercise_properties(self, exercise:str) -> dict:
        """Takes exercise in format of natural language. Give it to the exercise endpoint website(Nutritionix) for evaluation.
        Takes the evaluations from the website and returns it as in list format.

        Args:
            exercise (str): Exercise(s) in natural language format.

        Returns:
            list: List of the exercises. Contains calories, duration etc.
        """
        parameters = {
            "query": exercise,
            "age": self.age,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height
        }
        exercise_response = requests.post(url=self.exercise_endpoint, json=parameters, headers=self.header_exercise)
        exercise_exception_message = "Error by getting response from website Nutritionix. Please check APP ID or/and APP Key."
        self.check_response(response_code=exercise_response.status_code, exception_message=exercise_exception_message)
        exercise_list = self.check_exercise_data(exercise_data=exercise_response.json()["exercises"])
        return exercise_list
        
        
    def get_rows(self) -> None:
        """First checks the endpoints if they're exist and valid.
        Second checks the sheet name if it's valid too.
        If sheet name is not defined(empty), asks user for sheet name.
        At the end, Prints the rows of the saved google sheet.
        """
        self.check_endpoints()
        sheet_response = requests.get(url=self.sheet_endpoint, headers=self.header_sheet)
        
        sheet_exception_message = "Error by getting response from sheet. Please check the Auth token or/and connection betweenn website Sheety and google sheet."
        self.check_response(response_code=sheet_response.status_code, exception_message=sheet_exception_message)
        
        self.sheet_name = self.check_sheet_name(sheet_name=self.sheet_name, input_message="Please enter the sheet name of yours from website Sheety: ")
        rows = sheet_response.json()[self.sheet_name]
        for row in rows:
            print(f"Date: {row['date']}, exercise: {row['exercise']}, calorie: {row['calories']}")
    
    
    def get_calories(self, exercise:str) -> None:
        """Prints the exercise(s) and its/theirs calories burned(estimated).
        
        Args:
            exercise (str): Description of the exercise(s) in natural language.
        """
        exercise_list = self.get_exercise_properties(exercise=exercise)
        for exercise in exercise_list:
            print(f"Exercise: {exercise['exercise']}, Calorie burned(estimated): {exercise['calories']}")
            
    def get_exercise_url(self) -> str:
        return self.exercise_endpoint
    
    def get_sheet_url(self) -> str:
        return self.sheet_endpoint
    
    def get_sheet_name(self) -> str:
        return self.sheet_name
    
    def get_gender(self) -> str:
        return self.gender
    
    def get_height(self) -> str:
        return self.height
    
    def get_weight(self) -> str:
        return self.weight
    
    def get_age(self) -> str:
        return self.age
    
    # SETTERS
    def set_personal_properties(self, gender:str, age:int, height:int, weight:int) -> None:
        self.set_gender(gender=gender)
        self.set_age(age=age)
        self.set_height(height=height)
        self.set_weight(weight=weight)
            
    
    def set_sheet_infos(self, sheet_name:str, sheet_endpoint:str, authorization:str="") -> None:
        """Sets the sheet infos for the assigned sheet url. If sheet url has an authorization method, authorization information
        should be given too.

        Args:
            sheet_name (str): Sheet name of the project from the website Sheety.
            authorization (str, optional): Authorization token for the sheet(Basic or Bearer). Defaults to "".
        """
        if authorization != "":
            self.set_auth_token(auth_token=authorization)
        self.set_sheet_url(sheet_url=sheet_endpoint)
        self.set_sheet_name(sheet_name=sheet_name)
        
        
    def set_account_infos(self, app_id:str, app_key:str) -> None:
        """Takes 2 args and gives these arguments to the checkers functions to be checked if they're valid.

        Args:
            app_id (str): APP Id of the user from website Sheety.
            app_key (str): APP Key of the user from website Sheety.
        """
        self.set_app_id(app_id=app_id)
        self.set_app_key(app_key=app_key)
            
    def set_app_id(self, app_id:str) -> None:
        self.header_exercise["x-app-id"] = self.check_special_keys(special_key=app_id, exception_message="Length of APP ID cannot be shorter or equal to 0.")
    
    def set_app_key(self, app_key:str) -> None:
        self.header_exercise["x-app-key"] = self.check_special_keys(special_key=app_key, exception_message="Length of APP Key cannot be shorter or equal to 0.")
        
    def set_auth_token(self, auth_token:str) -> None:
        self.header_sheet["Authorization"] = self.check_special_keys(special_key=auth_token, exception_message="Length of Auth token cannot be shorter or equal to 0.") 
    
    def set_exercise_url(self, exercise_url:str) -> None:
        """Checks the given exercise url if it's valid or not and then assigns 
        the given url as new endpoint of exercises, if the URL is valid.

        Args:
            url (str): Url of the exercises from website Nutritionix.
        """
        self.exercise_endpoint = self.check_url(url=exercise_url)
        
    def set_sheet_url(self, sheet_url:str) -> None:
        """Checks the given sheet endpoint url if it's valid or not and then assigns 
        the given url as new endpoint of sheet, if the URL is valid.

        Args:
            url (str): Url of the sheet from website Sheety.
        """
        self.sheet_endpoint = self.check_url(url=sheet_url)
    
    def set_sheet_name(self, sheet_name:str) -> None:
        self.sheet_name = self.check_sheet_name(sheet_name=sheet_name, input_message="Please enter the sheet name of yours from website Sheety: ")
    
    def set_weight(self, weight:int) -> None:
        self.weight = self.check_weight(weight=weight)
    
    def set_gender(self, gender:str) -> None:
        self.gender = self.check_gender(gender=gender)
    
    def set_height(self, height:int) -> None:
        self.height = self.check_height(height=height)
    
    def set_age(self, age:int) -> None:
        self.age = self.check_age(age=age)