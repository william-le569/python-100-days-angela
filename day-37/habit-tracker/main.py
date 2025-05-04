import requests
from datetime import datetime

USERNAME = "billle"
TOKEN = "asdsadsad"
# GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
} # Create user

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# we get: https://pixe.la/v1/users/billle/graphs/graph1

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
today = datetime.now()

# test-section:
today = datetime(year=2025, month=5, day=4)

# date: yyyyMMdd
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

post_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(f"post reponse: {post_response}")

# -------------------UPDATE PIXEL---------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_data['date']}"

update_pixel_data = {
    "quantity": "100"
}

update_response = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)
print(f"update response: {update_response}")

#---------------------DELETE PIXEL ----------------------
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_data['date']}"

delete_reponse = requests.delete(url=delete_endpoint, headers=headers)
print(f"delete response: {delete_reponse}")