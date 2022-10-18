# 생일축하 메세지 Email 자동 전송 프로젝트 
import pandas
import random
from smtplib import SMTP
from datetime import datetime

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(content.month, content.day) : content for (index, content) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    f_path = f"letter_templates/letter_{random.randint(1,3)}"
    with open(f_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with SMTP("smtp.naver.com") as connect:
        connect.starttls()
        connect.login("blabla@naver.com", "1234abcd!")
        connect.sendmail(
            from_addr="blabla@naver.com",
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n {contents}"
        )





