import smtplib

my_email = "kyottest@gmail.com"
password = "jkbujogthwkazofw"
other_email = "emirpisirici@hotmail.com"
# Depending of the mail type that we're sending email from, server name changes.
# If someone sends email with his gmail, smtp.gmail.com suits good.
# But in case when someone sends mail with his yahoo or outlook, smtp server should change too.
# for yahoo -> smtp.mail.yahoo.com
# for gmail -> smtp.gmail.com
smtp_server = "smtp.gmail.com"

# Create connection with 'with' keyword. (Advantage: connection will be closed at the end by itself.)
with smtplib.SMTP(smtp_server) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=other_email, 
                        msg="Subject:Important.\n\nTesting the body of the email."
                        )