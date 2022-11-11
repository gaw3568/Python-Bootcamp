import requests
from pprint import pprint

PRICES_ENDPOINT = "Sheety_API_ENDPOINT"
USERS_ENDPOINT = "Sheety_API_ENDPOINT"
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for each_city in self.destination_data:
            update_data = {
                "price" : {
                    "iataCode" : each_city["iataCode"]
                }
            }
            requests.put(url=f"{PRICES_ENDPOINT}/{each_city['id']}", json=update_data)

    def get_customer_emails(self):
        customers_endpoint = USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
