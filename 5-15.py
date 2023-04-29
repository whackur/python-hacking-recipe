# pip install --upgrade pip
# pip install packaging
# pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://shop.hakhub.net"


def load_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 시스템에 부착된 장치 오류 제거
    options.add_argument("window-size=1920,1080")  # 창의 크기
    options.add_argument("lang=ko_KR")  # 한국어
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )


def get_item_info():
    driver.get(url)
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("li", {"class": "product"})
    for index, item in enumerate(items):
        print("================")
        print(f"{index+1}번째 상품", end="")
        print(item.text)
    driver.close()


if __name__ == "__main__":
    driver = load_driver()
    get_item_info()
