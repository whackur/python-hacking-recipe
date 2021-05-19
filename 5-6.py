import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

url = "https://shop.hakhub.net/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print("======= Title =======")
print(soup.title)
print("======= Head =======")
print(str(soup.head)[:300])
print("======= Head > Link =======")
print(soup.head.link)
print("======= Body =======")
print(str(soup.body)[:300])
