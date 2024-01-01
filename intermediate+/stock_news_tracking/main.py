# Program to understand why stock price of a company lost value
# Compare yesterdays and 2 days before values

import requests
import os
from twilio.rest import Client

# Define constants
MY_NUMBER = os.environ.get("MY_NUMBER")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
URL_STOCK = ("https://www.alphavantage.co/query")
URL_NEWS = ("https://newsapi.org/v2/everything")
COMPANY_NAME = "Tesla Inc"
STOCK_NAME = "TSLA"

# Define parameters for stock api(alphavantage)
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "apikey": STOCK_API_KEY,
    "symbol": STOCK_NAME,
}

# Get the response from stock api
response_stock = requests.get(url=URL_STOCK, params=parameters_stock)

# Check for status of connection
response_stock.raise_for_status()

# Take data in json format
data_stock = response_stock.json()
data_stock_time_series = data_stock["Time Series (Daily)"]

# Extract the keys and values
data_stock_list = [value for (key,value) in data_stock_time_series.items()]
data_stock_keys = [key for (key,value) in data_stock_time_series.items()]

# Take yesterdays and day before yesterdays closing prices
yesterday_data = data_stock_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_stock_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Calculate the difference between them and percentage of it
emoji = None
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if difference > 0:
    emoji = "🔼" 
else:
    emoji = "🔽"

# Do somethings according to the percentage
diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)
if abs(diff_percent) > 1:
    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "from": "",
        "apiKey": NEWS_API_KEY,
    }
    parameters_news["from"] = data_stock_keys[0]
    response_news = requests.get(url=URL_NEWS, params=parameters_news)
    response_news.raise_for_status()
    articles = response_news.json()["articles"]
    three_articles = articles[:3]
    summary = [f"{STOCK_NAME}: {emoji}{diff_percent}% \nHeadline:{article['title']}.\nBrief: {article['description']}" for article in three_articles]
    
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in summary:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )


