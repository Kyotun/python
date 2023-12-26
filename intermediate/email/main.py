import smtplib

my_email = "kyottest@gmail.com"
password = "jkbujogthwkazofw"
other_email = "emirpisirici@hotmail.com"

# Create connection with 'with' keyword. (Advantage: connection will be closed at the end by itself.)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=other_email, 
                        msg="Subject:Important.\n\nTesting the body of the email."
                        )