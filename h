import requests

# Your API key
api_key = "jaBTaztirF6uau1w7EOlBiosi8YqSEEn"

# Example: Get company profile for Apple (AAPL)
url = f"https://financialmodelingprep.com/api/v3/profile/AAPL?apikey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)