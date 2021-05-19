from selenium import webdriver

url = "https://shop.hakhub.net"


def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")  # 창의 크기
    options.add_argument("lang=ko_KR")  # 한국어
    return webdriver.Chrome("drivers/chromedriver", options=options)


def add_cart():
    driver.get(url)
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="main"]/ul/li[1]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="main"]/ul/li[2]/a[2]').click()
    driver.find_element_by_css_selector(
        "#main > ul > li.product.type-product.post-53.status-publish.instock.product_cat-clothing.product_cat-hoodies.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"
    ).click()
    driver.find_element_by_css_selector(
        "#main > ul > li.product.type-product.post-31.status-publish.last.instock.product_cat-clothing.product_cat-t-shirts.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"
    ).click()


if __name__ == "__main__":
    driver = load_driver()
    add_cart()
