"""HTTP base samples"""
import requests

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

response = requests.get(url=URL)
assert response.status_code == 200
data = response.json()
for currency in data:
    print(f"Course of {currency['ccy']} is {currency['buy']}")
