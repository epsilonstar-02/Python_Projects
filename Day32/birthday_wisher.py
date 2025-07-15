import pandas as pd
import datetime as dt
import random
import smtplib
import os

birthdays = pd.read_csv(os.path.join(os.path.dirname(__file__), "birthdays.csv"))

now = dt.datetime.now()
today = (now.month, now.day)

for _, row in birthdays.iterrows():
    if (row['month'], row['day']) == today:
        template_path = os.path.join(os.path.dirname(__file__), "letter_templates", f"letter_{random.randint(1,3)}.txt")
        with open(template_path) as letter_file:
            content = letter_file.read().replace("[NAME]", row['name'])
        my_email = "your_email@example.com"
        my_password = "your_password"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row['email'],
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )
