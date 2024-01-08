import requests
import os
import datetime as dt
from tracker_exception import TrackerException
import validators

APP_ID = os.environ.get("APP_ID_NUTRI")
APP_KEY = os.environ.get("APP_KEY_NUTRI")
AUTH_KEY_BEARER = os.environ.get("APP_AUTH_NUTRI")

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
        self.sheet_endpoint:str = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/workouts/tabellenblatt1"
        self.sheet_name:str = ""
        
        self.set_personal_properties()
        self.set_account_infos()
        
    def add_exercise(self) -> None:
        """Checks first if endpoints and sheet name are valid. Then asks user the exercise(s). For given exercise(s)
        create row(s) in given sheet.
        """
        date_today = dt.datetime.now().strftime("%d/%m/%Y")
        time_now = dt.datetime.now().strftime("%X")
        
        self.check_endpoints()
        self.check_sheet_name(sheet_name=self.sheet_name, input_message="Please enter the sheet name: ")
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
    
    # CHECKERS
    def check_app_id(self, app_id:str) -> TrackerException or str:
        """Checks the given app id. If its length <= 0, raises a TrackerException.

        Args:
            app_id (str): App ID of sheety account.

        Raises:
            TrackerException: Exception, for to show the reason to user.

        Returns:
            TrackerException or str: If length <= 0, a TrackerException will be raised.
            In case of success -> APP ID will be returned.
        """
        if len(app_id) <= 0:
            raise TrackerException(message="Length of APP Id cannot be shorter or equal to 0.")
        return app_id
    
    def check_app_key(self, app_key:str) -> TrackerException or str:
        """Checks the given app key. If its length <= 0, raises a TrackerException.

        Args:
            app_key (str): APP KEY of sheety account.

        Raises:
            TrackerException: Exception, for to show the reason to user.

        Returns:
            TrackerException or str:  If length <= 0, a TrackerException will be raised.
            In case of success -> APP KEY will be returned.
        """
        if len(app_key) <= 0:
            raise TrackerException(message="Length of APP Key cannot be shorter or equal to 0.")
        return app_key
    
    def check_auth_token(self, auth_token:str) -> TrackerException or str:
        """Checks the given auth token. If its length <= 0, raises a TrackerException.

        Args:
            auth_token (str): Auth Token of sheety account.

        Raises:
            TrackerException: Exception, for to show the reason to user.

        Returns:
            TrackerException or str: If length <= 0, a TrackerException will be raised.
            In case of success -> Auth Token will be returned.
        """
        if len(auth_token) <= 0:
            raise TrackerException(message="Length of Auth token cannot be shorter or equal to 0.")
        return auth_token
    
    def check_endpoints(self):
        """Checks the URL of the exercise and sheet endpoints. If there is a empty one, asks user for the URL.
        """
        exercise_message = "Please give the URL of the exercise endpoint from nutritionix website."
        sheet_endpoint_message = "Please give the URL of the sheet endpoint from sheety."
        self.exercise_endpoint = self.check_url(url=self.exercise_endpoint, input_message=exercise_message)
        self.sheet_endpoint = self.check_url(url=self.sheet_endpoint, input_message=sheet_endpoint_message)
        
    def check_url(self, url:str, input_message:str) -> Exception or str:
        """Checks the given URL if it is empty string or not.
        If it's a empty one, asks user for its URL and then validates it.
        If response is 200, returns the url. If not 200, raises an exception.

        Args:
            url (str): URL to be controlled.
            input_message (str): Message for asking user for the URL.

        Raises:
            TrackerException: Exception, for to show the reason of the error to user.
            
        Returns:
            Exception or str: If URL isn't valid, an exception will be retuned.
            If it's valid, url will be retuned.
        """
        if url == "":
            url = input(input_message)
        if validators.url(url) == False:
            raise TrackerException(message=f"{url} is not valid.")
        return url
    
    def check_sheet_name(self, sheet_name:str, input_message:str) -> str:
        """Checks the given sheet name if it is empty string or not.
        If it's a empty string, asks user with given input message for its name.

        Args:
            sheet_name (str): Name of the sheet(excel document).
            input_message (str): Will be shown while asking user the sheet name.

        Returns:
            str: Sheet name in string data type.
        """
        if sheet_name == "":
            sheet_name = input(input_message)
        return sheet_name
            
    def check_weight(self, weight:int) -> int or Exception:
        """Checks the weight, if it's in a logical range it will be accepted and will be returned.
        If not in logical range, an exception will be raised.

        Args:
            weight (int): Weight of the user in integer type.

        Raises:
            TrackerException: Exception, for to show the reason to user.

        Returns:
            int or Exception: If no exception, weight will be returned.
        """
        if weight < 0 or weight > 200:
            raise TrackerException(message="Weight should be between 0-200")
        return weight
    
    def check_gender(self, gender:str) -> str or Exception:
        """Checks the gender of the user. Only two gender will be allowed.

        Args:
            gender (str): Male or Female.(Not case sensitive)

        Raises:
            TrackerException: Exception, for to show the reason to user.

        Returns:
            int or Exception: If the given gender is logical, gender will be retuned. If not, an exception
            will be raised.
        """
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
        print(response, json_data, response.text)
        return json_data
        
        
    def get_rows(self) -> None:
        """Prints the rows of the target google sheet.
        If sheet name is not pre-defined, asks user for sheet name.
        """
        self.check_endpoints()
        response = requests.get(url=self.sheet_endpoint, headers=self.headers)
        if self.sheet_name == "":
            self.sheet_name = input("Please enter the sheet name from sheety:")
        if self.sheet_name not in response.json():
            raise TrackerException(message="Please check and consider changing the sheeet name again.")
        rows = response.json()[self.sheet_name]
        for row in rows:
            print(f"Date: {row['date']}, exercise: {row['exercise']}, calorie: {row['calories']}")
    
    # SETTERS
    def set_personal_properties(self) -> None:
        """Asks user to his/hers physical properties for accurate evaluation.
        Inputs should be in a logical range. If they're not, an exception will be raised.
        """
        self.set_gender()
        self.set_age()
        self.set_height()
        self.set_weight()
            
            
    def set_account_infos(self) -> None:
        """Asks user to the APP ID, APP Key. If there is no, they will be stay as empty string.
        Lastly it asks the auth token, if there is an auth method and sets these given variables
        as self variables.
        """
        self.headers["x-app-id"] = self.check_app_id(input("Please enter your Nutritionix APP ID: "))
        self.headers["x-app-key"] = self.check_app_key(input("Please enter your Nutritionix APP Key: "))
        if(input("Is there a auth method? 'y' or 'n': ") == 'y'):
            self.headers["Authorization"] = self.check_auth_token(input("Please enter the token(in format -> Basic/Bearer TOKEN): "))
            
            
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
    
    def set_weight(self) -> None:
        """First checks the weight then assigns it as new weight.
        """
        self.weight = self.check_weight(int(input("Please enter your weight in kg: ")))
    
    def set_gender(self) -> None:
        """First checks the gender then assigns it as new gender.
        """
        self.gender = self.check_gender(input("Please enter your gender: ").lower())
    
    def set_height(self) -> None:
        """First checks the height then assigns it as new height.
        """
        self.height = self.check_height(int(input("Please enter your height in cm: ")))
    
    def set_age(self) -> None:
        """First checks the age then assigns it as new age.
        """
        self.age = self.check_age(int(input("Please enter your age: ")))