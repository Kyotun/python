import requests
import os
import datetime as dt
from workout_tracker import WorkoutTracker

NUTRI_API_ID = os.environ.get("APP_ID_NUTRI")
NUTRI_API_KEY = os.environ.get("APP_KEY_NUTRI")
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 180
AGE = 22

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/workouts/tabellenblatt1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "content-type": "application/json",
    "x-app-id": NUTRI_API_ID,
    "x-app-key": NUTRI_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

date_today = dt.datetime.now().strftime("%d/%m/%Y")
time_now = dt.datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "tabellenblatt1": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response)
    print(sheet_response.text)