import requests
from twilio.rest import Client

# Save the constants
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 50.937531
MY_LONG = 6.960279
API_KEY = "f94f959a8d3503ac7b79a86547c68a96"
auth_token = "230660536be485bc744bd5cdb1ee295d"
account_sid = "AC3cd2243550ac55bbcd13b5bac421abd8"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid": API_KEY
}

# Get the response from openweathermap website and save the json data.
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Iterate through the json data and find the rainy timeline, if there is.
# If there is a timeline that will rain, send a message.
rain = False
for timline in weather_data["list"]:
    condition_code = timline["weather"][0]["id"]
    if int(condition_code) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_="+15208299098",
        to="+" #Your number here
    )
    print(message.status)