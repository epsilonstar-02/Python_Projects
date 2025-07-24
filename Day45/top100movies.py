with open("movies.html", "r") as file:
    content = file.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, "html.parser")
movies = soup.select(selector="span.content_content__i0P3p h2 strong")
movies = movies[::-1]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{str(movie.text)}\n")