import requests
import datetime as dt

MY_LAT = 50.937531
MY_LNG = 6.960279
FORMAT = 0
# Save the lat and longitude of your location with help latlong.net
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": FORMAT
}

# 'response' stores the website infos.
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

# will raise an error if something is wrong.
response.raise_for_status()

# Save json in 'data'. 'data' stores informations as dict.
data = response.json()

# Take the sunset and sunrise datas from data and format them into clearer version
# Convert them into integer to be able to compare
sunset = int(data["results"]["sunset"].split("T")[1].split("+")[0])
sunrise = int(data["results"]["sunrise"].split("T")[1].split("+")[0])

# Save the time of now with help of datetime module
now = dt.datetime.now()
# Format it same like sunset and sunrise
now_time = f"{now.hour}:{now.minute}:{now.second}"

# Show them with ausput
print(sunrise)
print(now_time)
print(sunset)
