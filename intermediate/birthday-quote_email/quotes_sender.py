import datetime as dt
import smtplib
import random

MY_EMAIL = "kyottest@gmail.com"
MY_PASSWORD = "Kytest60."
OTHER_EMAIL = "emirpisirici@hotmail.com"


# If today is monday, a quote will be selected randomly from quotes.txt.
# A connection will be opened and an email will be sended via my email to target email.
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("intermediate/email_datetime/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=OTHER_EMAIL, 
                            msg=f"Subject:Monday Motivation ;)\n\n{random_quote}")