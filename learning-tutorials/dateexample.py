#!/usr/bin/python3.8

from datetime import date
import time
from datetime import datetime
from datetime import timedelta

## 24 hour format
print(time.strftime("%H:%M:%S"))

## 12 hour format ##
print(time.strftime("%I:%M:%S"))

print('******************************************')
todaywithtime = datetime.today()

today = date.today()
fdate = date.today().strftime('%d/%m/%Y')

print(today.month)

print("Today's current date is -", today)
print("Today's current date is -", todaywithtime)

print("Date in dd/mm/YYYY format -", fdate)

print('******************************************')
t = timedelta(days=4, hours=10)

print("You still have " + str(t.days) + " days")
print("You have " + str(t.seconds) + " seconds")

print('******************************************')
eta = timedelta(hours=6)
today1 = datetime.today()

print(today1)
print(eta)
print(today1 + eta)
print(today1 - eta)

## 24 hours format date convertion to different format
instr = (today1 - eta).strftime('%d/%m/%Y %H:%M:%S')
print(instr)

print('******************************************')
STR = "24 HOURS FORMAT DATE CONVERTION TO DIFFERENT FORMAT"
print(STR.lower())

print('******************************************')

## using eta1 ti test all if condition scenarios
eta1 = timedelta(days=0)
christmas = date(2020, 12, 25)
date_today = date.today() + eta1

if date_today > christmas:
    print("Christmas passed " + str(abs((christmas - date_today)).days) + " days ago in " + str(
        christmas.year) + " year!!!!")
elif date_today < christmas:
    print("Christmas is " + str((christmas - date_today).days) + " days to go in " + str(christmas.year) + " year!!!!")
else:
    print('Hurry today is Christmas in ' + str(christmas.year) + ' year!!!!')

print('******************************************')
eta2 = timedelta(days=2, hours=6)

print('Time Delta Value: ' + str(eta2))
print('Days part: ' + str(eta2.days))
print('Seconds part: ' + str(eta2.seconds))
print('In hours: ' + str(eta2.seconds/3600))

