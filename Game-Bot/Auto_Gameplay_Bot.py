import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://orteil.dashnet.org/experiments/cookie/"
# Chrome drive path 설정
chrome_drive_path = "Your chrome driver path"

# 브라우저 꺼짐 현상 해결
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_drive_path, options=chrome_options)
driver.get(url=URL)

# cookie 이미지
cookie = driver.find_element(By.ID, "cookie")

# 구매 목록들의 ID 값
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]

# 시간 측정
timeout = time.time() + 5
five_minutes = time.time() + 60 * 5     # 300초 = 5분

while True:
    cookie.click()

    if time.time() > timeout:
        # 구매할 수 있는 아이템에 필요한 쿠키의 수
        items_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        price_list = []

        for price in items_price:
            if price.text != "":
                revised_price = int(price.text.split("-")[1].strip().replace(",",""))
                price_list.append(revised_price)

        # item_price와 items_id를 매칭하여 dictionary로 저장
        cookie_purchase_dict = {}

        for index in range(len(price_list)):
            cookie_purchase_dict[price_list[index]] = items_id[index]

        # 현재 보유한 쿠키
        current_cookie = driver.find_element(By.ID, "money").text

        if "," in current_cookie:
            current_cookie = int(current_cookie.replace(",", ""))
        current_cookie = int(current_cookie)

        # current_cookie와 cookie_purchase_dict의 price를 비교하여 구매가능한 item을 리스트업

        buying_items = {}

        for price, id in cookie_purchase_dict.items():
            if current_cookie >= price:
                buying_items[price] = id

        # buying_items에서 구매할 수 있는 가장 비싼 아이템을 구매
        expensive_item_price = max(buying_items)
        expensive_item_price_id = buying_items[expensive_item_price]

        driver.find_element(By.ID, expensive_item_price_id).click()

        timeout = time.time() + 5
    
    if time.time() > five_minutes:
        print(driver.find_element(By.CSS_SELECTOR, "#saveMenu div").text)
        break
    
