import requests
from bs4 import BeautifulSoup
from time import time
import asyncio
import aiohttp  # pip install aiohttp aiodns cchardet
import json

page_urls = ["https://shop.hakhub.net/page/1/", "https://shop.hakhub.net/page/2/"]
json_path = "./comments.json"


def get_product_urls(urls):
    """
    모든 상품의 URL 반환
    """
    product_urls = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        elem_li = soup.find_all("li", {"class": "product"})
        for li in elem_li:
            product_urls.append(li.find("a")["href"])
    print(f"{len(product_urls)}개의 상품이 존재합니다.")
    return product_urls


async def asnyc_func(urls):
    # 같은 TCP Session 사용
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as s:
        futures = [asyncio.create_task(show_product_review(s, url)) for url in urls]
        results = await asyncio.gather(*futures)
    with open(json_path, "w", encoding="utf-8") as f:
        print(f"JSON file save as: {json_path}")
        json.dump(results, f, indent=4, ensure_ascii=False)


async def show_product_review(s, url):
    async with s.get(url) as r:
        html = await r.text()
    soup = BeautifulSoup(html, "html.parser")
    product_name = soup.find("h1").text
    comments = soup.find_all("div", {"class": "comment-text"})
    comment_dict = {}
    comment_dict["product_name"] = product_name
    comment_array = []
    for comment in comments:
        comment_array.append(
            {
                "author": comment.find(
                    "strong", {"class": "woocommerce-review__author"}
                ).text,
                "rating": comment.find("strong", {"class": "rating"}).text,
                "datetime": comment.find("time")["datetime"],
                "description": comment.find("div", {"class": "description"}).text,
            }
        )
    comment_dict["comments"] = comment_array
    return comment_dict


if __name__ == "__main__":
    begin = time()
    product_urls = get_product_urls(page_urls)
    asyncio.run(asnyc_func(product_urls))
    end = time()
    print(f"실행 시간: {end - begin}")
