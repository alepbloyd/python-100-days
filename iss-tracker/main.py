import requests
import datetime as dt
import smtplib
import time

MY_LAT = 38.907192
MY_LNG = -77.036873

GMAIL_TEST_EMAIL = "alepbloyd.test@gmail.com"
GMAIL_TEST_PASSWORD = ""

YAHOO_TEST_EMAIL = "alepbloyd.test@yahoo.com"

GMAIL_CONNECTION = smtplib.SMTP("smtp.gmail.com", port=587)
YAHOO_CONNECTION = smtplib.SMTP("smtp.mail.yahoo.com")

def iss_in_range():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_latitude = float(iss_response.json()['iss_position']['latitude'])
    iss_longitude = float(iss_response.json()['iss_position']['longitude'])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
        MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
    ):
        return True
    else:
        return False
    
def is_dark():
    sunrise_sunset_parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
    }

    sunrise_sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sunrise_sunset_parameters)
    sunrise_sunset_response.raise_for_status()

    sunrise_sunset_data = sunrise_sunset_response.json()

    sunrise = sunrise_sunset_data['results']['sunrise']
    sunrise_time = sunrise.split('T')[1]
    sunrise_hour = int(sunrise_time.split(":")[0])
    sunrise_minute = int(sunrise_time.split(":")[1])

    sunset = sunrise_sunset_data['results']['sunset']
    sunset_time = sunset.split('T')[1]
    sunset_hour = int(sunset_time.split(":")[0])
    sunset_minute = int(sunset_time.split(":")[1])

    time_now = dt.datetime.now()
    if (
        time_now.hour + (time_now.minute / 60) < sunrise_hour + (sunrise_minute / 60) or
        time_now.hour + (time_now.minute / 60) > sunset_hour + (sunset_minute / 60)
    ):
        return True
    else:
        return False

def send_message():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_TEST_EMAIL, password=GMAIL_TEST_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_TEST_EMAIL,
            to_addrs=YAHOO_TEST_EMAIL,
            msg=f"Subject:ISS overhead alert.\n\n Wow look up"
        )

while True:
    time.sleep(60)
    if iss_in_range() and is_dark():
        send_message()