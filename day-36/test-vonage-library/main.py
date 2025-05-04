import os
# import vonage
# import vonage_http_client 
# from vonage import Client, Sms

# Vonate ver 4.4.1
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

from my_config import from_num, to_num 

vonage_api_key = os.environ.get("VONAGE_API_KEY")
vonage_api_secret_key = os.environ.get("VONAGE_API_SECRET_KEY")

# ----------------------- this is ver 2.6.0 -----------------------
# client = vonage.Client(key=vonage_api_key, secret=vonage_api_secret_key)
# client = vonage.Auth(api_key=vonage_api_key, api_secret=vonage_api_secret_key)
# sms = vonage.Sms(client)
# responseData = sms.send_message(
#     {
#         "from": from_num,
#         "to": to_num,
#         "text": "Hello World! from Bill Le",
#     }
# )

# if responseData["messages"][0]["status"] == "0":
#     print("Message sent successfully.")
# else:
#     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

client = Vonage(Auth(api_key=vonage_api_key, api_secret=vonage_api_secret_key))

message = SmsMessage(
    to=to_num,
    from_=from_num,
    text="This is test message from Bill for educational purposes.",
)

response: SmsResponse = client.sms.send(message)
print(response)
