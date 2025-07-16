import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
position = data["iss_position"]
latitude = position["latitude"]
longitude = position["longitude"]
print(f"The ISS is currently at latitude {latitude} and longitude {longitude}.")
