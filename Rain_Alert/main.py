import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""

api_end_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69c3dce0fd3877d13db588557459c8f1"
# Suwon si - 위도, 경도
my_lat = 37.2658097
my_lon = 126.9999102

# key : value 의 형태로 prameter의 dictionary에 저장.
weather_parameters = {
    "lat" : my_lat,
    "lon" : my_lon,
    "appid" : api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_end_point, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     # 임시번호
                     from_='+15017122661',
                     # 임시번호
                     to='+15558675310' 
    )
    print(message.status)