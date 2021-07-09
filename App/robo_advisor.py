import os

from requests.models import DEFAULT_REDIRECT_LIMIT
from dotenv import load_dotenv
import requests
import json
#from sengrid import SendGridAPIClient

load_dotenv()
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
# make a request
symbol = input("Which symbol would you like data for:") 
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)
time_series_data = json.loads(response.text)

print("-------------------------")
print("SELECTED SYMBOL:", "Meta ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
date = time_series_data["Meta Data"]["3. Last Refreshed"]
print("REQUEST AT:", date)
print("-------------------------")
print("LATEST CLOSE:",  time_series_data["Time Series (Daily)"][date]["4. close"])
print("RECENT HIGH: 101,000.00")
# print("RECENT LOW: $99,000.00")
# print("-------------------------")
# print("RECOMMENDATION: BUY!")
# print("RECOMMENDATION REASON: TODO")
# print("-------------------------")
# print("HAPPY INVESTING!")
# print("-------------------------")
#print(Time_series_data)


