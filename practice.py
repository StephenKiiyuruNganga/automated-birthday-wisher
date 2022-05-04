import datetime as dt

now = dt.datetime.now()
print(now)
print(now.year)

# monday - 0, tue - 1, etc...
print(now.weekday())

date_of_birth = dt.datetime(year=1993, month=4, day=10)
print(date_of_birth)
