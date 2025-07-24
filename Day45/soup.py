from bs4 import BeautifulSoup
import pandas as pd


with open("news.html","r") as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")
title = soup.select(selector="td.title span a")
upvotes = [int(i.text.split()[0]) for i in soup.find_all(name="span", class_="score")]
articles = [i.text for i in title]
article_title = articles[::2]
article_link = articles[1::2]

news = pd.DataFrame(columns=["title","link","upvotes"])
news["title"] = article_title
news["link"] = article_link
news["upvotes"] = upvotes


news.sort_values(by="upvotes", ascending=False).to_csv("articles.csv", index=False)