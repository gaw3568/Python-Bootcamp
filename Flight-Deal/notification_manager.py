<<<<<<< HEAD
from smtplib import SMTP

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_emails(self, emails, message, google_flight_link):
        with SMTP("smtp.gmail.com", 587) as connect:
            connect.starttls()
            connect.login("MY_EMAIL_ADDR","MY_EMAIL_PSWD")
            for each_email in emails:
                connect.sendmail(
                    from_addr = "MY_EMAIL_ADDR",
                    to_addr = each_email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
=======
# Twilio API를 사용하여 구글시트에 저장된 금액보다 저렴하면 SMS로 전송
# 코드 수정 예정

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass
>>>>>>> refs/remotes/origin/main
