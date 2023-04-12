import smtplib
import datetime as dt
import random

GMAIL_TEST_EMAIL = "alepbloyd.test@gmail.com"
GMAIL_TEST_PASSWORD = ""

YAHOO_TEST_EMAIL = "alepbloyd.test@yahoo.com"

GMAIL_CONNECTION = smtplib.SMTP("smtp.gmail.com", port=587)
YAHOO_CONNECTION = smtplib.SMTP("smtp.mail.yahoo.com")

with open("quotes.txt", mode="r") as quote_file:
  quotes = quote_file.readlines()

random_quote = random.choice(quotes)

now = dt.datetime.now()

if now.weekday() == 1:
  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=GMAIL_TEST_EMAIL, password=GMAIL_TEST_PASSWORD)
    connection.sendmail(
                        from_addr=GMAIL_TEST_EMAIL,
                        to_addrs=YAHOO_TEST_EMAIL,
                        msg=f"Subject:Motivational Quote\n\n{random_quote}."
    )