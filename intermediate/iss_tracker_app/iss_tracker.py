# Program for:
    # Look for ISS Location in format of longitude and latitude
    # Take longitude and latitude of users current location
    # If ISS close to users curent location and its dark outside for user
        # Send email to user to go out and look up.
import smtplib
import requests
import datetime as dt


MY_LAT = 50.937531
MY_LNG = 6.960279
FORMAT = 0
MY_EMAIL = "kyottest@gmail.com"
TARGET_EMAIL = "emirpisirici@hotmail.com"
PASSWORD = "jkbujogthwkazofw"
SMTP_SERVER = "smtp.gmail.com"

# Save the lat and longitude of your location with help latlong.net
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": FORMAT
}

def converter(param):
    """Check if the given splitted datetime parameter close to the higher end of current time slice.
    if given a list -> ["15", "36", "33"], return will be 16.
    if given a list -> ["06", "24", "25"], return will be 6.
    """
        
    if int(param[1]) > 30:
        param = int(param[0]) + 1
    else:
        param = int(param[0])
    return param


def is_dark():
    """Calculates if time of now bigger then sunset or smaller then sunrise, returns True. Otherwise false.
    """
    
    # 'response' stores the website infos.
    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    # will raise an error if something is wrong.
    response_sun.raise_for_status()

    # Save json in 'data'. 'data' stores informations as dict.
    data_sun = response_sun.json()

    # Take the sunset and sunrise datas from data and format them into clearer version
    # Convert them into integer to be able to compare
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split("+")[0])
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split("+")[0])
    sunset = converter(sunset)
    sunrise = converter(sunrise)

    # Save the time of now with help of datetime module
    now = dt.datetime.now()
    if now.hour > sunset or now.hour < sunrise:
        return True
    return False


def calculate_iss_distance():
    """Calculates the abs of longitude and latitude of users current location.
    If both of them are smaller or equal then 5, returns True.
    """
    
    # 'response' stores the website infos.
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")

    # will raise an error if something is wrong.
    response_iss.raise_for_status()

    # Save json in 'data'. 'data' stores informations as dict.
    data_iss = response_iss.json()

    iss_longitude = float(data_iss["iss_position"]["longitude"])
    iss_latitude = float(data_iss["iss_position"]["latitude"])
    lat_dist = abs(MY_LAT - iss_latitude)
    lng_dist = abs(MY_LNG - iss_longitude)
    if lat_dist <= 5 and lng_dist <= 5:
        return True
    return False

    
def send_mail():
    """Send mail to the target mail from 'MY_EMAIL' to warn the user to look up for ISS.
    """
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=TARGET_EMAIL, 
                            msg=f"Subject:ISS is there!\n\nGo out and look up to see the ISS!"
                            )
        


if calculate_iss_distance() and is_dark():
    send_mail()
