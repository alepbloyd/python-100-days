STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import requests
import os
import json
from twilio.rest import Client
from stock_day import StockDay
from article import Article

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

av_url = "https://www.alphavantage.co/query"

av_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY,
    "outputsize": "compact",
    "datatype": "json"
}

av_response = requests.get(url = av_url,
                        params = av_params)

av_json_response = json.loads(av_response.text)

daily_time_series = av_json_response["Time Series (Daily)"]

days = [StockDay(day) for day in daily_time_series.items()]

yesterday = days[0]
day_before_yesterday = days[1]

closing_percent_change = round(((yesterday.close_price - day_before_yesterday.close_price) / yesterday.close_price) * 100, 4)

if abs(closing_percent_change >= 5):
  new_api_url = "https://newsapi.org/v2/everything"

  news_header = {"X-Api-Key": NEWS_API_KEY}
  news_params = {
      "q": COMPANY_NAME,
      "pageSize": 3
  }

  news_response = requests.get(url = new_api_url,
                              headers = news_header,
                              params= news_params)

  news_json_response = json.loads(news_response.text)

  article_list = [Article(article_dict) for article_dict in news_json_response["articles"]]
  
  text_body = f"""
  {STOCK}: {"🔺" if closing_percent_change >= 0 else "🔻"}{closing_percent_change}%
  Headline: {article_list[0].title}
  Brief: {article_list[0].description}
  -----
  Headline: {article_list[1].title}
  Brief: {article_list[1].description}
  -----
  Headline: {article_list[2].title}
  Brief: {article_list[2].title}
  """

  twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

  message = twilio_client.messages.create(
      body = text_body,
      to=os.environ.get("PHONE_TO"),
      from_=os.environ.get("PHONE_FROM")
  )

  print(message.status)