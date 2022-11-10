from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import *
from datetime import datetime, timedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for each_data in sheet_data:
        each_data["iataCode"] = flight_search.get_destination_code(each_data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
after_six_month = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight_search.check_flight(
        origin_city_code=ORIGIN_CITY_IATA, 
        destination_city_code=destination["iataCode"], 
        from_time=tomorrow, 
        to_time=after_six_month
    )
