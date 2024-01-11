import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_APP_KEY = os.environ.get("APP_KEY_TEQUILA")

class FlightSearch():
    def __init__(self) -> None:
        self.header_tequila = {
            "apikey": TEQUILA_APP_KEY,
        }
    
    def get_destination_code(self, city_name:str) -> str:
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"term": city_name, "location_type": "city"}
        response = requests.get(url=endpoint, headers=self.header_tequila, params=query)
        json_data = response.json()
        location = json_data["locations"]
        iataCode = location[0]["code"]
        return iataCode
    
    def check_flights(self, from_city_code, to_city_code, from_time, to_time):
        query = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=self.header_tequila,
            params=query,
        )
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found from {from_city_code} to {to_city_code}.")
            return None
            
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.get_to_city()}: {flight_data.get_price()}")
        return flight_data