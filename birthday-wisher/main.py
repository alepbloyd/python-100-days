import smtplib
import datetime as dt
import pandas
import random

GMAIL_TEST_EMAIL = "alepbloyd.test@gmail.com"
GMAIL_TEST_PASSWORD = ""

YAHOO_TEST_EMAIL = "alepbloyd.test@yahoo.com"

GMAIL_CONNECTION = smtplib.SMTP("smtp.gmail.com", port=587)
YAHOO_CONNECTION = smtplib.SMTP("smtp.mail.yahoo.com")

birthdays = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
today_month = now.month
today_day = now.day

letters = []
for i in range(1,4):
  with open(f"letter_templates/letter_{i}.txt", mode="r") as letter:
    letters.append(letter.read())

random_letter = random.choice(letters)

for index,row in birthdays.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        message = random_letter.replace("[NAME]", row['name'])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
          connection.starttls()
          connection.login(user=GMAIL_TEST_EMAIL, password=GMAIL_TEST_PASSWORD)
          connection.sendmail(
                        from_addr=GMAIL_TEST_EMAIL,
                        to_addrs=YAHOO_TEST_EMAIL,
                        msg=f"Subject:Happy Birthday!\n\n{message}."
          )


