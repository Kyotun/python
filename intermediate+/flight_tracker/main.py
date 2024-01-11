from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY_IATA = "IST"
DAY_IN_MONTH = 30
MONTH_NUMBER = 6
LOWER_END_DATE = datetime.now() + timedelta(days=1)
HIGHER_END_DATE = datetime.now() + timedelta(days=(DAY_IN_MONTH*MONTH_NUMBER)) 

data_manager = DataManager()
flight_search = FlightSearch()
    
is_on = True
while is_on:
    print("Options:")
    print("1)Load the google sheet datas.")
    print("2)Update the destination codes of cities.")
    print("3)Change the origin city code.")
    print("4)Add new city to the google sheet.")
    print("5)Check price from a city to other city.")
    print("6)Exit.")
    answer = input("Please a number of an option: ")
    
    if answer == 1:
        pass
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        pass
    elif answer == 5:
        pass
    elif answer == 6:
        pass
    elif answer == 7:
        pass
    elif answer == 8:
        pass
    
    
    data_manager, sheet_data = create_data_manager()
    flight_search = FlightSearch()

    for destination in sheet_data:
        flight = flight_search.check_flights(
            from_city_code=ORIGIN_CITY_IATA,
            to_city_code=destination["iataCode"],
            from_time=LOWER_END_DATE,
            to_time=HIGHER_END_DATE
        )