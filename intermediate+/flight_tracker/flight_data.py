import requests
import os
import datetime as dt


TEQUILA_APP_KEY = os.environ.get("APP_KEY_TEQUILA")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2"

class FlightData():
    def __init__(self, price:int,
                 origin_city:str, 
                 origin_airport:str, 
                 destination_city:str, 
                 destination_airport:str, 
                 out_date:str, 
                 return_date:str) -> None:
        self.price = price
        self.from_city = origin_city
        self.from_airport = origin_airport
        self.to_city = destination_city
        self.to_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
    
    def get_price(self) -> int:
        return self.price
    
    def get_from_city(self) -> str:
        return self.from_city
    
    def get_from_airport(self) -> str:
        return self.from_airport
    
    def get_to_city(self) -> str:
        return self.to_city
    
    def get_to_airport(self) -> str:
        return self.to_airport
    
    def get_out_date(self) -> str:
        return self.out_date
    
    def get_return_date(self) -> str:
        return self.return_date
    
    def set_price(self, price:int) -> None:
        self.price = price
    
    def set_from_city(self, from_city:str) -> None:
        self.from_city = from_city
        
    def set_from_airport(self, from_airport:str) -> None:
        self.from_airport= from_airport
        
    def set_to_city(self, to_city:str) -> None:
        self.to_city = to_city
    
    def set_to_airport(self, to_airport:str) -> None:
        self.to_airport = to_airport
    
    def set_out_date(self, out_date:str) -> None:
        self.out_date = out_date
    
    def set_return_date(self, return_date:str) -> None:
        self.return_date = return_date
