import subprocess
import sys

# Automatically install requests if it's missing
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
print("requests installed successfully!")


import requests

API_KEY = "YOUR_API_KEY_HERE"
symbol = "AAPL"

url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"
response = requests.get(url)
data = response.json()

if data:
    stock = data[0]
    print(f"{stock['symbol']}: ${stock['price']}")
else:
    print("No data found.")