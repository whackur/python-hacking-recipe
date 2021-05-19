from selenium import webdriver

url = "https://shop.hakhub.net"

user_login = "customer01"
user_pass = "customer01!!"


def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")  # 창의 크기
    options.add_argument("lang=ko_KR")  # 한국어
    return webdriver.Chrome("drivers/chromedriver", options=options)


def get_product_title():
    driver.get(url)
    driver.implicitly_wait(3)
    elements = driver.find_elements_by_class_name("woocommerce-loop-product__title")
    for element in elements:
        print(element.text)


if __name__ == "__main__":
    driver = load_driver()
    get_product_title()
