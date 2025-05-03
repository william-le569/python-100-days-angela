import requests
import os
from twilio.rest import Client

OPM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
# Vinh Long location.
MY_LAT = 10.253956
MY_LONG = 105.963393

DALAT_LAT = 11.890465
DALAT_LONG = 108.432741

# weather_params = {
#     'lat': MY_LAT,
#     'lon': MY_LONG,
#     'appid': api_key,
#     'cnt': 4
# }

# Testcase with Dalat

weather_params = {
    'lat': DALAT_LAT,
    'lon': DALAT_LONG,
    'appid': api_key,
    'cnt': 4
}

# Retrieve those from Twilio Dashboard.
account_sid = ""
auth_token= ""
client = Client(account_sid, auth_token)

response = requests.get(OPM_endpoint, params=weather_params)
response.raise_for_status()
status_code = response.status_code
weather_data = response.json()

print(status_code)
# print(weather_data)

will_rain = False
for hour_data in weather_data["list"]:
    item_weather_code = hour_data['weather'][0]['id']
    item_weather_date = hour_data['dt_txt']
    if item_weather_code < 700:
        print(f"Bring umbrella! on {item_weather_date}")
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring umbrella!☂️",
        from_="+16203106473",
        to="+13136525082",
    )
    print(message.status)
