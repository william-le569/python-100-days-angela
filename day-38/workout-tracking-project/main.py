import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "45"
HEIGHT_CM = "164"
AGE = "26"

nutri_app_id = os.environ.get("NUTRI_APP_ID")
nutri_app_key = os.environ.get("NUTRI_APP_KEY")
sheety_bearer_token = os.environ.get("SHEETY_BEARER_TOKEN")
sheety_endpoint = os.environ.get("SHEET_ENDPOINT")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# exercise_text = input("Tell me which exercises you did: ")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': nutri_app_id ,
    'x-app-key': nutri_app_key 
}

# params = {
#     "query":"1 cup mashed potatoes and 2 tbsp gravy"
# }
# I don't know how to get those parameter
is_run = True
while is_run:
    exercise_text = input("Tell me which exercises you did: ")
    if exercise_text != "exit":
        parameters = {
            "query": exercise_text,
            "gender": GENDER,
            "weight_kg": WEIGHT_KG,
            "height_cm": HEIGHT_CM,
            "age": AGE
        }

        response = requests.post(url=nutri_endpoint, json=parameters, headers=headers)

        result = response.json()

        # print(result)

        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        print(result["exercises"])

        for exercise in result["exercises"]:
            sheet_input = {
                "workout": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }


        # OPTION 1: No Authentication.

        # sheety_response = requests.post(url=sheety_endpoint, json=sheet_input)

        # print(sheety_response.text)

        # OPTION 2: Basic Authentication.

        # sheety_response = requests.post(
        #     sheety_endpoint,
        #     json=sheet_input,
        #     auth = {
        #         YOURUSERNAME,
        #         YOURPASSWORD,
        #     }
        # )

        # Bearer Token Authentication
        bearer_headers = {
            "Authorization": f"Bearer {sheety_bearer_token}"
        }

        sheety_response = requests.post(
            sheety_endpoint,
            json=sheet_input,
            headers=bearer_headers
        )

        print(sheety_response)
     
    else:
        is_run = False

