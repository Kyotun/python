import requests

# 'response' stores the website infos.
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# will raise an error if something is wrong.
response.raise_for_status()

# Save json in 'data'. 'data' stores informations as dict.
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)
