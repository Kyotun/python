import requests

SHEETY_ENDPOINT = "https://api.sheety.co/04fb3676394a9afdc57d00b4868f30df/flightDeals/tabellenblatt1"

class DataManager():
    def __init__(self) -> None:
        self.sheet_endpoint = SHEETY_ENDPOINT
        self.destination_data = {}
        self.header_sheety = {
            "Authorization": ""
        }
    
    # SETTERS
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
        json_data = response_sheet.json()
        self.destination_data = json_data[self.get_sheet_name()]
    
    # Check destination data first if it's empty
    def update_destination_codes(self):
        from flight_search import FlightSearch
        flight_search = FlightSearch()
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
            