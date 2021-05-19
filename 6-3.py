import requests
from bs4 import BeautifulSoup, SoupStrainer

target_domain = "https://shop.hakhub.net"
content = requests.get(target_domain).content

links = set()
for link in BeautifulSoup(
    content, features="html.parser", parse_only=SoupStrainer("a")
):
    if hasattr(link, "href"):
        path = link["href"]
        if target_domain not in path and path[:4] != "http":
            links.add(target_domain + path)
        else:
            links.add(path)

for link in links:
    print(link)
