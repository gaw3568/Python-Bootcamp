import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2"

response = requests.get(url=URL)

movies_web_page = response.text

soup = BeautifulSoup(movies_web_page,'html.parser')

title = soup.find(name='h1', class_="jsx-928984976 title")

test_list = soup.find_all(name="img", class_="jsx-952983560")[1:]
test_list.reverse()

movie_list = [f"{i+1}) {movie.get('alt')}" for i, movie in enumerate(test_list)]

with open(file="movie_checklist.txt", mode="w") as file:
    for rank in movie_list:
        file.write(f"{rank}\n")