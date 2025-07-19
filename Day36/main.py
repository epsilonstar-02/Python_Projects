import datetime as dt
import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

yesterday = str(dt.date.today() - dt.timedelta(days = 1))
day_before = str(dt.date.today() - dt.timedelta(days=2))
params_stock = {
    "function" : os.getenv("FUNC"),
    "symbol" : os.getenv("STOCK"),
    "apikey" : os.getenv("ALPHAVANTAGE_API_KEY"),
}

params_news = {
    "apiKey" : os.getenv("NEWS_API_KEY"),
    "q" : os.getenv("COMPANY_NAME"),
    "pageSize" : 3,
}

def get_news():
    news = requests.get(url=os.getenv("NEWS_URL"), params=params_news)
    news.raise_for_status()
    news = [i for i in news.json()["articles"]]
    send_sms(news, fluctuation)


def send_sms(articles, change):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    percent = abs(round(change * 100))
    arrow = "🔺" if change > 0 else "🔻"
    stock_msg = f"{os.getenv('STOCK')}: {arrow}{percent}%\n"

    for article in articles:
        message = f"{stock_msg}Headline: {article['title']}\nBrief: {article['description']}"

        client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("YOUR_PHONE_NUMBER")
        )


data = requests.get(url=os.getenv("STOCK_URL"), params=params_stock)
data.raise_for_status()
stock_yesterday = data.json()["Time Series (Daily)"][yesterday]
stock_day_before = data.json()["Time Series (Daily)"][day_before]
yest = stock_yesterday["4. close"]
day_before = stock_day_before["4. close"]
fluctuation = (float(yest) - float(day_before))/float(day_before)
if abs(fluctuation) > 0.05:
    get_news()
