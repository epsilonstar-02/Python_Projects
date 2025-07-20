import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

print("Welcome to the Flight Club!")
print("We find the best flight deals and email them to you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What is your email?\n")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Type your email again.\n")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()
    if email1 != email2:
        print("Emails do not match. Please try again.")

print("You're in the club!")

new_data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email1,
    }
}

response = requests.post(
    url=SHEETY_USERS_ENDPOINT,
    json=new_data
)

response.raise_for_status()
print(response.text)

