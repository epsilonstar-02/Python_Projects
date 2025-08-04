import requests

LAT=22.572645
LON=88.363892
params = {
    "lat" : LAT,
    "lon" : LON,
    "appid" : "api-key",
}

weather = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=params)
weather.raise_for_status()
data = weather.json()

# Extract and print current weather details
current = data.get("current", {})
temp = current.get("temp")
weather_desc = current.get("weather", [{}])[0].get("description")

print(f"Current temperature: {temp}K")
print(f"Weather description: {weather_desc}")

# Print hourly forecast for next 12 hours
print("\nHourly forecast (next 12 hours):")
hourly = data.get("hourly", [])
for hour in hourly[:12]:
    dt = hour.get("dt")
    temp = hour.get("temp")
    desc = hour.get("weather", [{}])[0].get("description")
    print(f"Time: {dt}, Temp: {temp}K, Description: {desc}")
