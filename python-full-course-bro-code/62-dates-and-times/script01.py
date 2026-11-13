import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2027, 1, 2, 12, 30, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date passed")
elif target_datetime == current_datetime:
    print("Target date is now")
else:
    print("Target date has not passed")

print(date)
print(today)

print(time)
print(now)