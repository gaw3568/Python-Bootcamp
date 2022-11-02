import requests
from twilio.rest import Client

STOCK_API_KEY = "R2Z1JILPNAJJ2SVM"
NEWS_API_KEY = "bda10003933448e79ac8eaebc9678361"

TWILIO_SID = "ACf8c7516f9bc19898e330427e89d58e3a"
TWILIO_AUTH_TOKEN = "d448f033405d0eb81641ec6b61f6648d"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

news_params = {
    "q" : COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language" : "en"
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (_,value) in data.items()]       # 최근 날짜 2022-11-01 부터 데이터 저장
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference =  float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_of_difference = round((difference / float(yesterday_closing_price)) * 100)
print(percent_of_difference)

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(percent_of_difference) >= 0:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    article_list = [f"{STOCK_NAME} : {up_down}{percent_of_difference}% \nHeadline : {article['title']}. \nBrief : {article['description']}" for article in three_articles]
    
    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    for each_article in article_list:    
        message = client.messages.create(
            body = each_article,
            from_ = '+821073103567',     # twilio 가상번호
            to = '+821073103567'         # 내 번호 (받을 사람)
        )

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

