# Game bot을 활용한 Cookie-Clicker Game Automation 프로젝트
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

GAME_URL = "https://orteil.dashnet.org/cookieclicker/"

CHROME_DRIVER = "/Users/jewon/Development/chromedriver"

MAX_MINUTES = time.time() + 60 * 5

# 브라우저 꺼짐 현상 해결
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Chrome Driver를 드라이버에 연결 및 지정된 URL 주소 불러오기
driver = webdriver.Chrome(CHROME_DRIVER, options=chrome_options)
driver.get(url=GAME_URL)
driver.maximize_window()

# Web Page 로딩 시간을 고려한 time모듈 실행.
time.sleep(3)


# item 이름 잠금 해제 전 (???)
# for item in products_secret:
#     print(driver.find_element(By.CLASS_NAME, item.get_attribute("class")).text)
# print("total : ", len(products_secret))

# 언어 선택
languages_id = driver.find_elements(By.CSS_SELECTOR, ".langSelectButton")
language_list = [language.get_attribute("id") for language in languages_id]
choose_language = language_list.index("langSelect-EN")
driver.find_element(By.ID, language_list[choose_language]).click()

time.sleep(3)
RESET_TIMEOUT = time.time() + 5

while True:
    # Cookie ID 불러오기
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()
    
    if time.time() > RESET_TIMEOUT:
        # 구매가능한 아이템에 필요한 쿠키 수량 저장
        products_price = driver.find_elements(By.CSS_SELECTOR, ".price")
        price_list = []
        for product in products_price:
            price = driver.find_element(By.ID, product.get_attribute("id")).text
            if "," in price:
                price = int(price.replace(",", ""))
                price_list.append(int(price))
            else:
                if price != "":
                    price_list.append(int(price))

        # 구매가능한 아이템 Class값 저장
        products_name = driver.find_elements(By.CSS_SELECTOR, "#products div")
        name_list = [name.get_attribute("id") for name in products_name]
        print(name_list)

        # 각 아이템 쿠키의 개수, 아이템 ID를 매칭하여 dictionary 자료형으로 저장
        purchase_cookie_dict = {}
        for index in range(len(price_list)):
            purchase_cookie_dict[price_list[index]] = name_list[index]

        # 현재 보유하고있는 쿠키 수
        current_having_cookie = driver.find_element(By.ID, "cookies").text.split()[0]
        if "," in current_having_cookie:
            current_having_cookie = int(current_having_cookie.replace(",", ""))
        current_having_cookie = int(current_having_cookie)

        # current_cookie와 cookie_purchase_dict의 price를 비교하여 구매가능한 item을 리스트업
        buying_items = {}
        for price, id in purchase_cookie_dict.items():
            if current_having_cookie >= price:
                buying_items[price] = id

        # 구매가능한 목록 중 최고 금액으로 살 수 있는 아이템을 선택
        expensive_item_price = max(buying_items)
        expensive_item_price_id = buying_items[expensive_item_price]
        driver.find_element(By.CLASS_NAME, expensive_item_price_id).click()

        RESET_TIMEOUT = time.time() + 5

    if time.time() > MAX_MINUTES:
        break