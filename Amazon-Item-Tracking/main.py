import requests
import lxml
from smtplib import SMTP
from bs4 import BeautifulSoup

LIMIT_PRICE = 100

URL = "https://www.amazon.com/SAMSUNG-Portable-SSD-1TB-MU-PC1T0H/dp/B0874YJP92?ref_=Oct_DLandingS_D_2675836c_60"

HEADER = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language" : "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=URL, headers=HEADER)

web_page = response.content

soup = BeautifulSoup(web_page, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()

# 상품 판매 가격
price_without_currency = float(price.split("$")[1])

# 상품명
product_title = soup.find(name="span", id="productTitle").getText().strip()

if price_without_currency < LIMIT_PRICE:
    message = f"{product_title} is now {price_without_currency}"
    print(message)
 
