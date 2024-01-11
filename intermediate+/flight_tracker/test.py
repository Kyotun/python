import os
import requests
from datetime import datetime, timedelta
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_APP_KEY = os.environ.get("APP_KEY_TEQUILA")
header_tequila = {
    "apikey": TEQUILA_APP_KEY,
}

# city_code = "ASDASDasd"
# city_name = "Cologne"

# endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
# query = {"term": city_code, "location_type": "city"}
# response = requests.get(url=endpoint, headers=header_tequila, params=query)
# print(response.text)
# print(response.status_code)
# locations = response.json()["locations"]
# first_row = locations[0]
# first_name = first_row["name"]

DAY_IN_MONTH = 30
MONTH_NUMBER = 6
LOWER_END_DATE = datetime.now() + timedelta(days=1)
HIGHER_END_DATE = datetime.now() + timedelta(days=(DAY_IN_MONTH*MONTH_NUMBER)) 
from_time = LOWER_END_DATE.strftime("%d/%m/%Y")
to_time = HIGHER_END_DATE.strftime("%d/%m/%Y")
query = {
            "fly_from": "CGN",
            "fly_to": "IST",
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        
response = requests.get(
    url=f"{TEQUILA_ENDPOINT}/v2/search",
    headers=header_tequila,
    params=query,
)

print(response.text)

