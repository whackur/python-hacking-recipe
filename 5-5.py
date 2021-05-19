import requests

url = "https://shop.hakhub.net/"

r = requests.get(url)
print(r.text)
