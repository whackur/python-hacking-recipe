# pip install --upgrade pip
# pip install packaging
# pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://shop.hakhub.net"

user_login = "customer01"
user_pass = "customer01!!"


def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")  # 창의 크기
    options.add_argument("lang=ko_KR")  # 한국어
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )


def get_product_title():
    driver.get(url)
    driver.implicitly_wait(3)
    elements = driver.find_elements(By.CLASS_NAME, "woocommerce-loop-product__title")
    for element in elements:
        print(element.text)


if __name__ == "__main__":
    driver = load_driver()
    get_product_title()
