import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


soup = BeautifulSoup(page.text, "html.parser")


# знайти перший тег <p> на сторінці
first_paragraph = soup.find("p")

