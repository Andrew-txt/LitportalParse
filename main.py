import json

import requests
from bs4 import BeautifulSoup

URL = "https://litportal.ru/"
HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")

main_container = soup.find("div", class_="Layout_mainContainer__wrap___XfDm")
content_wrapper = main_container.find("div")
scrollable_content = content_wrapper.find("div", class_="Home_slider__z1jBh")
books_container = scrollable_content.find("div", class_="scrollbar_art scrollbar scrollbar_parent") # контейнер со списком книг из раздела краткое содержание

books = books_container.find_all("div", class_="undefined scroll_item")
books_json = []

for book in books:
    book_title = book.find("a", class_="HomeSliderItem_slide__title__tCRfz").get_text(strip=True)
    book_author = book.find("a", class_="HomeSliderItem_slide__author__I3sns").get_text(strip=True)

    books_json.append({
        "book_title": book_title,
        "book_author": book_author
    })

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books_json, file, indent=4, ensure_ascii=False)
