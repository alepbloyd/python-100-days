import requests
from twilio.rest import Client
import json
import os

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

#DC
LAT = 38.9072
LON = 77.0369

open_weather_url = f"https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": OPENWEATHER_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url = open_weather_url,
                        params = weather_params)

response.raise_for_status()

weather_data = response.json()

hourly_data = weather_data['hourly']

next_12_hours = hourly_data[0:12]

next_12_hours_codes = [hour['weather'][0]['id'] for hour in next_12_hours]

if any(weather_code < 700 for weather_code in next_12_hours_codes):
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = twilio_client.messages.create(
        body="☔️☔️☔️ It's going to rain ☔️☔️☔️",
        to='+19193608871',
        from_='+18338798877'
    )

    print(message.status)