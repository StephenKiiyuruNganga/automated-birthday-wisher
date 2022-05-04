import random
import datetime as dt
import smtplib

my_email = "tests.steveknganga@gmail.com"
my_password = "A&wIrFQ25i2N"

with open("quotes.txt") as file:
    content = file.readlines()
    converted_content = [line.strip("\n ").split("-")
                         for line in content]
    quotes = [{"quote": item[0],
               "person": item[1].strip(" ")}
              for item in converted_content]
    random_quote = random.choice(quotes)
    weekday = dt.datetime.now().weekday()
    if weekday == 2:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="tests.steveknganga@yahoo.com",
                                msg=f"Subject: Happy Wednesday!\n\n{random_quote['quote']}\n- {random_quote['person']}")
