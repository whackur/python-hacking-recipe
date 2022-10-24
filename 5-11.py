# pip install --upgrade pip
# pip install packaging
# pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from PIL import Image  # pip install pillow

url = "https://shop.hakhub.net/product/flying-ninja/"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")  # 창의 크기
options.add_argument("lang=ko_KR")  # 한국어

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.get(url)
driver.implicitly_wait(3)
driver.get_screenshot_as_file("web.png")

Image.open("web.png").convert("RGB").save("web.jpg", quality=100)
im = Image.open("web.jpg")
cropped_image = im.crop((280, 300, 1100, 780))
cropped_image.save("web_cropped.jpg", quality=100)

driver.close()
