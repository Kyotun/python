import requests
from flight_exception import FlightTrackerException

SHEETY_ENDPOINT = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/flightDeals/tabellenblatt1"

class DataManager():
    def __init__(self) -> None:
        self.sheet_endpoint = SHEETY_ENDPOINT
        self.destination_data = {}
        self.header_sheety = {
            "Authorization": ""
        }
    
    # SETTERS
    def set_new_city(self, city_name:str) -> None:
        self.check_data()
        self.check_city(city_name=city_name)
        city_number = len(self.destination_data)
        new_city = {
            "tabellenblatt1": {
                "city": city_name
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{city_number+1}", json=new_city)
        
    def set_destination_data(self, data:dict) -> None:
        self.destination_data = data
        
    # GETTERS
    def get_sheet_name(self) -> str:
        sheet_name = self.sheet_endpoint.split("/")[-1]
        return sheet_name
    
    def get_destination_datas(self) -> dict:
        return self.destination_data
    
    # UPDATES
    def load_destination_data(self) -> None:
        response_sheet = requests.get(url=self.sheet_endpoint, headers=self.header_sheety)
        exception_message = "Error by reaching to google sheet with Sheety. Please control the auth token or/and connection to URL."
        self.check_response(response_code=response_sheet, exception_message=exception_message)
        json_data = response_sheet.json()
        self.destination_data = json_data[self.get_sheet_name()]
    
    # Check destination data first if it's empty
    def update_destination_codes(self):
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        self.check_data()
        for city in self.destination_data:
            city_name = city['city']
            iataCode = flight_search.get_destination_code(city_name=city_name)
            new_data = {
                "tabellenblatt1": {
                    "iataCode": iataCode
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
    
    # CHECKERS
    def check_data(self) -> FlightTrackerException or None:
        if len(self.destination_data) < 1:
            raise FlightTrackerException(message="There is no destination data.")
        return None
    
    def check_city(self, city_name:str) -> FlightTrackerException or None:
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        flight_search.check_city_parameter(city_parameter=city_name)
    
    def check_response(self, response_code:str, exception_message:str) -> FlightTrackerException or None:
        if response_code != 200:
            raise FlightTrackerException(message=exception_message)
        return None
            