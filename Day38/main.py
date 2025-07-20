import json
import os
from dotenv import load_dotenv
import requests
import datetime as dt
load_dotenv(override=True)

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_url = os.getenv("EXERCISE_URL")
sheets_url = os.getenv("SHEETS_URL")

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

param = {
    "query": input("Tell me which exercise you did: "),
}

response = requests.post(url=exercise_url, json=param, headers=header)
response.raise_for_status()
print(json.dumps(response.json(),indent=4))

body = {
    "workout" : {
        "date": dt.datetime.strftime(dt.datetime.now(), "%d/%m/%Y"),
        "time": dt.datetime.strftime(dt.datetime.now(), "%H:%M:%S"),
        "exercise": response.json()["exercises"][0]["name"].title(),
        "duration": response.json()["exercises"][0]["duration_min"],
        "calories": response.json()["exercises"][0]["nf_calories"],
    }
}

sheets = requests.post(url=sheets_url, headers={"Authorization" : os.getenv("AUTH")},
                       json=body)
sheets.raise_for_status()
print(sheets.json())