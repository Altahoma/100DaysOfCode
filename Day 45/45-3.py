from requests_html import HTMLSession
from bs4 import BeautifulSoup

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "100_best_movies.html"


def get_web_page():
    session = HTMLSession()
    response = session.get(WEB_PAGE)
    response.html.render()

    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


result = read_web_file()
all_movies = result.find_all(name='h3', class_='jsx-4245974604')
movie_titles = [movie.text for movie in all_movies]
movies = movie_titles[::-1]
with open('movies.txt', 'w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
