import pandas as pd
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "kyottest@gmail.com"
PASSWORD = "jkbujogthwkazofw"
SMTP_SERVER = "smtp.gmail.com"


def pick_letter():
    with open(f"intermediate/email_datetime/letter_{random.randint(1,3)}.txt") as letter:
        letter_to_send = letter.read()
        letter.close()
    return letter_to_send
        
        
today = dt.datetime.now()
data = pd.read_csv("intermediate/email_datetime/birthdays.csv")
for index in range(len(data)):
    if data["month"][index] == today.month and data["day"][index] == today.day:
        letter_blueprint = pick_letter()
        letter_to_send = letter_blueprint.replace(PLACEHOLDER, data["name"][index])
        birthday_email = data["email"][index]

with smtplib.SMTP(SMTP_SERVER) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs=birthday_email, 
                        msg=f"Subject:Happy Birthday!\n\{letter_to_send}"
                        )

        