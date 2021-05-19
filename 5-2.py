import requests  # pip install requests

url = "https://shop.hakhub.net"
r = requests.get(url)
print(f"Status Code: {r.status_code}")
print(f"Response Header: {r.headers}")
print("Response Body")
print(r.text[:1000])
