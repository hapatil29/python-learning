#!/usr/bin/python3.8

from datetime import date
import time
from datetime import datetime

## 24 hour format
print(time.strftime("%H:%M:%S"))

## 12 hour format ##
print(time.strftime("%I:%M:%S"))

todaywithtime = datetime.today()

today = date.today()
fdate = date.today().strftime('%d/%m/%Y')

print(today.month)


print("Today's current date is -", today)
print("Today's current date is -", todaywithtime)

print("Date in dd/mm/YYYY format -", fdate)