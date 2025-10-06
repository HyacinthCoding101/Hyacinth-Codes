import requests

# Your FMP API key
API_KEY = "YOUR_API_KEY_HERE"

# Example: Get real-time quote for Apple
symbol = "AAPL"
url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"

# Send request
response = requests.get(url)

# Convert to JSON
data = response.json()

# Print stock info
if data:
    stock = data[0]
    print(f"Symbol: {stock['symbol']}")
    print(f"Price: ${stock['price']}")
    print(f"Change: {stock['change']} ({stock['changesPercentage']}%)")
else:
    print("No data found.")