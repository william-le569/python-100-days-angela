import datetime as dt
import random
import smtplib

MY_EMAIL = "bill.le9956@gmail.com"
MY_PASSWORD = "remember to delete the actual password."


now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 4:
    with open("quotes.txt", 'r') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # tls: Transport Layer Security.
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="thieu.le569@gmail.com",
            msg=f"Subject:Friday Motivation\n\n{quote}"
        )
