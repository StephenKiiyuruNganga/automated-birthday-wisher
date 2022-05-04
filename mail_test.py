import smtplib

my_email = "tests.steveknganga@gmail.com"
my_password = "A&wIrFQ25i2N"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # secure the connection - tls - translation layer security
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tests.steveknganga@yahoo.com",
                        msg="Subject:Hello Python World\n\nThe start of something great!")
