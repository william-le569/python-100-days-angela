##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import os
import random
import smtplib

now = dt.datetime.now()
current_date = now.day
current_month = now.month

PLACE_HOLDER = "[NAME]"
MY_EMAIL = "bill.le9956@gmail.com"
MY_PASSWORD = "Remember to delete before pushing to git repository."

data = pd.read_csv('birthdays.csv')
data_dict = data.to_dict(orient="records")

for index in range(len(data_dict)):
    if data_dict[index]['month'] == current_month and data_dict[index]['day'] == current_date:
        random_file = random.choice(os.listdir("./letter_templates")) # pick a random letter template.
        with open('./letter_templates/' + random_file) as letter_file:
            letter_contents = letter_file.read()
            new_letter_contents = letter_contents.replace(PLACE_HOLDER, data_dict[index]['name'])

            # Open this section if you want to create a offline letter.
            # with open(f"./letter_in_use_for_{data_dict[index]['name']}.txt", 'w') as letter_in_use:
            #     letter_in_use.write(new_letter_contents)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=data_dict[index]['email'],
                    msg=f"Subject:Happy Birthday To {data_dict[index]['name']}\n\n{new_letter_contents}"
                )





