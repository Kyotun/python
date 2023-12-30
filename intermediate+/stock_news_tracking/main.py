import requests
import os

API_KEY = os.environ.get("MY_API_KEY")
URL = f"https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "apikey": f"{API_KEY}",
    "symbol": "TSLA",
}

response = requests.get(url=URL,params=parameters)
response.raise_for_status()
data = response.json()
print(data)