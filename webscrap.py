import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
prices = []
ratings = []

for page in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        titles.append(title)
        prices.append(price)
        ratings.append(rating)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
})

df.to_csv("C:/Users/dhany/OneDrive/Desktop/Web Scraping/Books.csv", index=False)

print("Data Scraped Successfully!")