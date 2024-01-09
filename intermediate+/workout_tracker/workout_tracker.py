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
        
        self.headers:str= {"Authorization": AUTH_KEY_BEARER, 
                           "x-app-id": APP_ID, 
                           "x-app-key": APP_KEY, 
                           "content-type": "application/json"}
        self.exercise_endpoint:str = EXERCISE_ENDPOINT
        self.sheet_endpoint:str = SHEET_ENDPOINT
        self.sheet_name:str = ""
        
    def add_exercise(self, exercise:str) -> None:
        """Checks the endpoints and sheet name first then give the exercise(text from user in natural language)
        to the webiste Nutritionix. Gets the evaluated informations from the website in list format.
        Exercise list contains informations like calories burned, duration in min etc. for every exercise.
        Give these information to the given google sheet url in form of columns.
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
            sheet_response = requests.post(url=self.sheet_endpoint, json=sheet_inputs, headers=self.headers)
    
    # CHECKERS
    def check_app_id(self, app_id:str) -> TrackerException or str:
        """Checks the given app id. If its length <= 0, raises a TrackerException.

        Args:
            app_id (str): App ID of account from website Sheety.

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
            app_key (str): APP KEY of account from website Sheety.

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
        This auth token belongs to the specific project from webiste Sheety.

        Args:
            auth_token (str): Auth Token of the sheet from website Sheety.

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
        exercise_endpoint_message = "Please give the URL of the exercise endpoint from website Nutritionix: "
        sheet_endpoint_message = "Please give the URL of the sheet endpoint from website Sheety: "
        self.sheet_endpoint = self.check_url(url=self.sheet_endpoint, input_message=sheet_endpoint_message)
        self.exercise_endpoint = self.check_url(url=self.exercise_endpoint, input_message=exercise_endpoint_message)
        
    def check_url(self, url:str, input_message:str = "Given URL is empty, please give a valid URL: ") -> Exception or str:
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
        if not validators.url(url):
            raise TrackerException(message=f"{url} is not valid.")
        return url
    
    def check_sheet_name(self, sheet_name:str, input_message:str) -> str:
        """Checks the given sheet name if it is empty string or not.
        If it's a empty string, asks user with given input message for its name.

        Args:
            sheet_name (str): Name of the sheet(excel document).
            input_message (str): Will be shown while asking user the sheet name if it's empty.

        Returns:
            str: Sheet name in string data type.
        """
        sheet_name_from_sheet_endpoint = self.sheet_endpoint.split("/")[-1]
        if sheet_name == "":
            sheet_name = input(input_message)
        if sheet_name != sheet_name_from_sheet_endpoint:
            raise TrackerException(message=f"Given sheet name {sheet_name} doesn't match with sheet name of sheet endpoint url {sheet_name_from_sheet_endpoint}.")
        return sheet_name
            
            
    def check_exercise_data(self, exercise_list:str) -> Exception or str:
        """Checks the given exercise list. If its length is 0, raise an error to give warning to user.

        Args:
            exercise_list (str): Contains the exercises and their relevant informations.

        Raises:
            TrackerException: Exception, for to show the reason to user.

        Returns:
            Exception or str: If length is not 0, exercise list will be returned. Otherwise, an exception will occur.
        """
        if len(exercise_list) == 0:
            raise TrackerException(message="There is no matching exercise data. Please try to write your exercise entry again.")
        return exercise_list
        
        
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
        """Takes exercise in format of natural language. Give it to the exercise endpoint website(Nutritionix) for evaluation.
        Takes the evaluations from the website and returns it as in list format.

        Args:
            exercise (str): Exercise in natural language format.

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
        response = requests.post(url=self.exercise_endpoint, json=parameters, headers=self.headers)
        exercise_list = self.check_exercise_data(exercise_data=response.json()["exercises"])
        return exercise_list
        
        
    def get_rows(self) -> None:
        """First checks the endpoints if they're exist and valid.
        Second checks the sheet name if it's valid too.
        If sheet name is not defined(empty), asks user for sheet name.
        At the end, Prints the rows of the saved google sheet.
        """
        self.check_endpoints()
        response = requests.get(url=self.sheet_endpoint, headers=self.headers)
        self.sheet_name = self.check_sheet_name(sheet_name=self.sheet_name, input_message="Please enter the sheet name of yours from website Sheety: ")
        rows = response.json()[self.sheet_name]
        for row in rows:
            print(f"Date: {row['date']}, exercise: {row['exercise']}, calorie: {row['calories']}")
    
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
        """Takes 4 args. Gives these arguments to the functions, which they're belong.

        Args:
            gender (str): Gender of the user, to be assigned as new gender of the account. 2 options, 'male' or 'female'. Not case sensitive.
            age (int): Age of the user, to be assigned as new age of the account.
            height (int): Height of the user, to be assigned as new height of the account.
            weight (int): Weight of the user, to be assigned as new weight of the account.
        """
        self.set_gender(gender=gender)
        self.set_age(age=age)
        self.set_height(height=height)
        self.set_weight(weight=weight)
            
    
    def set_sheet_infos(self, sheet_name:str, authorization:str="") -> None:
        """Sets the sheet infos for the assigned sheet url. If sheet url has an authorization method, authorization information
        should be given too.

        Args:
            sheet_name (str): Sheet name of the project from the website Sheety.
            authorization (str, optional): Authorization token for the sheet(Basic or Bearer). Defaults to "".
        """
        if authorization != "":
            self.headers["Authorization"] = authorization
        self.set_sheet_name(sheet_name=sheet_name)
        
        
    def set_account_infos(self, app_id:str, app_key:str) -> None:
        """Takes 3 args and gives these arguments to the checkers functions to be checked if they're valid.

        Args:
            app_id (str): APP Id of the user from website Sheety.
            app_key (str): APP Key of the user from website Sheety.
            authorization (str, optional): Auth token of the user from website Sheety. Defaults to "".
        """
        self.headers["x-app-id"] = self.check_app_id(app_id=app_id)
        self.headers["x-app-key"] = self.check_app_key(app_key=app_key)
            
            
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
        """Checks the given sheet name if it's valid. Then changes the currently available sheet name with the given one.

        Args:
            sheet_name (str): String that contains the new sheet name, that will be changed with the old sheet name.
        """
        self.sheet_name = self.check_sheet_name(sheet_name=sheet_name)
    
    def set_weight(self, weight:int) -> None:
        """First checks the given weight, if it's in logical range, given weight will be assigned as new weight.
        """
        self.weight = self.check_weight(weight=weight)
    
    def set_gender(self, gender:str) -> None:
        """First checks the given gender, if it's in logical range, given height will be assigned as new height.
        """
        self.gender = self.check_gender(gender=gender)
    
    def set_height(self, height:int) -> None:
        """First checks the given height, if it's in logical range, given height will be assigned as new height.
        """
        self.height = self.check_height(height=height)
    
    def set_age(self, age:int) -> None:
        """First checks the given age, if it's in logical range, given age will be assigned as new age.
        """
        self.age = self.check_age(age=age)