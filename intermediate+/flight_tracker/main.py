from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
data_manager.load_destination_data()
data_manager.update_destination_codes()
data_manager.load_destination_data()
sheet_data = data_manager.get_destination_datas()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "IST"
DAY_IN_MONTH = 30
MONTH_NUMBER = 6

# tomorrow
lower_end_date = datetime.now() + timedelta(days=1)

# six month for this example
higher_end_date = datetime.now() + timedelta(days=(DAY_IN_MONTH*MONTH_NUMBER)) 

for destination in sheet_data:
    flight = flight_search.check_flights(
        from_city_code=ORIGIN_CITY_IATA,
        to_city_code=destination["iataCode"],
        from_time=lower_end_date,
        to_time=higher_end_date
    )