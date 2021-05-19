import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

url = "https://shop.hakhub.net/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
elem_li = soup.find_all("li", {"class": "product"})

for index, li in enumerate(elem_li):
    print(f"\n======={index+1}번 상품=======")
    print(li.find("h2", {"class": "woocommerce-loop-product__title"}).text)
    print(li.find("span", {"class": "price"}).text)
    try:
        print(li.find("strong", {"class": "rating"}).text)
    except Exception as e:
        print("가격정보 없음")
