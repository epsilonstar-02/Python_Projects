import requests
from datetime import datetime

parameters = {
    "lat": 51.5074,
    "lng": -0.1278,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(response.json()['results']['sunrise'])
print(response.json()['results']['sunset'])
