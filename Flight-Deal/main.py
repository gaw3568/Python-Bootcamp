from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for each_data in sheet_data:
        each_data["iataCode"] = flight_search.get_destination_code(each_data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

find_tomorrow = datetime.now() + timedelta(days=1)
find_after_six_month = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flight(
        origin_city_code=ORIGIN_CITY_IATA, 
        destination_city_code=destination["iataCode"], 
        from_time=find_tomorrow, 
        to_time=find_after_six_month
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        # Use customers Info saved in Google Sheet
        users = data_manager.get_customer_emails()
        emails = [each_user["email"] for each_user in users]
        names = [each_user["firstName"] for each_user in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        # If there are stop overs
        if flight.stop_overs > 0:
            message = f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_emails(emails, message, link)