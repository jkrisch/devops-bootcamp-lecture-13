import sys
import datetime

month = int(input("Which month were you born (1-12): "))
day = int(input("On which day: "))
today = datetime.date.today()
now = datetime.datetime.now()

if today < datetime.date(today.year,month,day):
    next_birthday = datetime.datetime.strptime(f"{today.year}-{month}-{day}", "%Y-%m-%d")
elif today > datetime.date(today.year,month,day):
    next_birthday = datetime.datetime.strptime(f"{today.year}-{month}-{day}", "%Y-%m-%d")
elif today == datetime.date(today.year,month,day):
    print("Oh nice. You're birthday is today. HAPPY BIRTHDAY!!!!")
    sys.exit()

timespan = next_birthday - now
hours, remainder = divmod(timespan.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"you have to wait {timespan.days} days, {hours} hours and {minutes} minutes until your next birthday")
