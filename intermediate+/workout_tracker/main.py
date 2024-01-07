import requests
import os

NUTRI_API_ID = os.environ.get("APP_ID_NUTRI")
NUTRI_API_KEY = os.environ.get("APP_KEY_NUTRI")
GENDER = input("Please enter your gender:")
WEIGHT_KG = input("Please enter your weight in kg:")
HEIGHT_CM = input("Please enter your height in cm:")
AGE = input("Please enter your age:")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = input("Which exercise(s) did you do?:")
headers = {
        "x-app-id": NUTRI_API_ID,
        "x-app-key": NUTRI_API_KEY
    }
parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
json_data = response.json()
print(json_data)