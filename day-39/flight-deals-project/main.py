import os
import requests
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# sheety_flight_deal_endpoint = os.environ.get("SHEETY_FLIGHT_DEAL_ENDPOINT")
# sheety_flight_deal_bearer_token = os.environ.get("SHEETY_FLIGHT_DEAL_BEARER_TOKEN")

# sheety_flight_deal_bearer_headers = {
#     "Authorization": f"Bearer {sheety_flight_deal_bearer_token}"
# }

# print(sheety_flight_deal_endpoint)

# sheety_response = requests.get(url=sheety_flight_deal_endpoint, headers=sheety_flight_deal_bearer_headers)

# print(sheety_response.json())

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    print(sheet_data[0]["iataCode"])
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()