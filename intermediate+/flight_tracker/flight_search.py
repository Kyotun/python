import os

APP_KEY_TEQUILA = os.environ.get("APP_KEY_TEQUILA")

class FlightSearch():
    def __init__(self) -> None:
        self.header_tequila = {
            "apikey": APP_KEY_TEQUILA,
        }
    
    # Use the tequila API for the codes. 
    # Probably -> 
    # aiata_code = requests.get(url="https://api.tequila.kiwi.com/v2/{SOMETHING}", 
    # json_data = PROBABLY CITY NAME DICT , 
    # headers=self.header_tequila)
    def get_destination_codes(self, city_name:str) -> str:
        iataCode = "000"
        return iataCode