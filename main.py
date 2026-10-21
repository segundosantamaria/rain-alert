import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from twilio.rest import Client
import smtplib
import time
# import os


mail = "y" #your credentials!
mail_2 = "y2" #your credentials!
pw= "y1" #your credentials!

openweather_endepoint = "https://api.open-meteo.com/v1/forecast"
api_key = "api" #your credentials!
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

api_key_twilio = "x" #your credentials!
api_secret = "x2"#your credentials!
account_sid = "x3"#your credentials!
client = Client(api_key_twilio, api_secret, account_sid)



weather_params = {"latitude":-34.603683,
"longitude":-58.381557,
"hourly":"precipitation",
"timezone":"America/Sao_Paulo",

    
}

responses = openmeteo.weather_api(openweather_endepoint,params=weather_params)
response = responses[0]
# print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
# print(f"Elevation: {response.Elevation()} m asl")
# print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
# print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

hourly = response.Hourly()
precipitation = hourly.Variables(0).ValuesAsNumpy()
next_12_hs = precipitation[:12]

times = pd.date_range(start=pd.to_datetime(hourly.Time(),unit="s",utc=True,),periods=12,freq="h")
times = times.tz_convert("America/Argentina/Buenos_Aires")


#Sms alert
# for i in range(12):
#     if next_12_hs[i] > 0:
#         message = client.messages.create(
#             body="sms_internal_alerts",
#             from_ ='+',
#             to = '+')
        
#         print(message.status)
#         print(times[i])
#     else:
#         message = client.messages.create(
#                 body="sms_internal_alerts",
#                 from_ ='+',
#                 to = '+')
#     # print("Weather is clear!")
    
#Email alert
def will_rain():
    for i in range(12):
        if next_12_hs[i] > 0.5:
            print(f"at {times[i]} will rain")
            return True
    return False


while True:
    time.sleep(3600)
    if will_rain():
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=mail,password=pw)
        connection.sendmail(from_addr=mail,to_addrs=mail_2, msg="Subject: Watch Out for the rain!\n\nBetter grab an umbrella if you are going out because it's going to rain")
        connection.close()
    else:
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=mail,password=pw)
        connection.sendmail(from_addr=mail,to_addrs=mail_2, msg="Subject: Weather update\n\n Weather should be clear for the next 12 hours :)")
        connection.close()
                  
              

