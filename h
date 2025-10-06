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



import requests

API_KEY = "YOUR_API_KEY_HERE"
symbol = "AAPL"

url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"
response = requests.get(url)

# Show what came back
print("Raw response:", response.text)

# Try converting to JSON
try:
    data = response.json()
except Exception as e:
    print("Error converting to JSON:", e)
    data = []

# Check and print data
if isinstance(data, list) and len(data) > 0:
    stock = data[0]
    print(f"Symbol: {stock['symbol']}")
    print(f"Price: ${stock['price']}")
else:
    print("⚠️ No valid stock data found.")