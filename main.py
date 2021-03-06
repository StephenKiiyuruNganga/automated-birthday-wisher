import random
import smtplib
import pandas
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "tests.steveknganga@gmail.com"
my_password = "A&wIrFQ25i2N"

df = pandas.read_csv("birthdays.csv")
birthdays_dict = [{"name": row["name"],
                   "email": row.email,
                   "year": row.year,
                   "month": row.month,
                   "day": row.day}
                  for (index, row) in df.iterrows()]

for person in birthdays_dict:
    if person["month"] == month and person["day"] == day:
        # prepare letter
        choice = random.randint(1, 3)
        with open(f"./letter_templates/letter_{choice}.txt") as file:
            content = file.readlines()
            content[0] = content[0].replace("[NAME]", person["name"])

            # send letter
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=person["email"],
                                    msg=f"Subject: Happy Birthday!\n\n{' '.join(content)}")
