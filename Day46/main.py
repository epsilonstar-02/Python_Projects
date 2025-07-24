from bs4 import BeautifulSoup
import requests

year = "2025-07-24"
url = f"https://www.billboard.com/charts/hot-100/{year}"
response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
response.raise_for_status()
content = response.text

with open("top100.html", "w") as file:
    file.write(content)

soup = BeautifulSoup(content, "html.parser")
tags = soup.select("li h3#title-of-a-story")
songs = [i.get_text().strip() for i in tags]
print(songs)

with open("songs.txt", "a") as file:
    for i in songs:
        file.write(f"{i}\n")