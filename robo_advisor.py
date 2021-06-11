import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
# make a request
symbol = "MSFT" # ask for a user input
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)

Time_series_data = json.loads(response.text)
print(Time_series_data)


