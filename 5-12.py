# pip install --upgrade pip
# pip install packaging
# pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://shop.hakhub.net/wp-login.php"

user_login = "customer01"
user_pass = "customer01!!"


def load_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 시스템에 부착된 장치 오류 제거
    options.add_argument("window-size=1920,1080")  # 창의 크기
    options.add_argument("lang=ko_KR")  # 한국어
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )


def try_login():
    driver.get(url)
    driver.implicitly_wait(3)

    driver.find_element(By.NAME, "log").send_keys(user_login)
    driver.find_element(By.NAME, "pwd").send_keys(user_pass)

    driver.find_element(By.NAME, "wp-submit").click()


if __name__ == "__main__":
    driver = load_driver()
    try_login()
