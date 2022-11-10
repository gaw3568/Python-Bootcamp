import requests
from pprint import pprint

ENDPOINT = "https://api.sheety.co/f86c55ff1f68b9236d2ad70b8662f2eb/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=ENDPOINT)
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
            response = requests.put(url=f"{ENDPOINT}/{each_city['id']}", json=update_data)
