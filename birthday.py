"""
birthday.py
Author: Will Campbell
Credit: Eli
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
import calendar
import datetime

from datetime import datetime
from calendar import month_name

todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]

name = input("Hi, what is your name? ") 
month = input("Hello "+name+", what was the name of the month you were born in? ")
year = int(input("And what year were you born in, "+name+"? "))
day = int(input("And the day? ") )

if month == "January":
    monthnumber = 1
elif month == "February":
    monthnumber = 2
elif month == "March":
    monthnumber = 3
elif month == "April":
    monthnumber = 4
elif month == "May":
    monthnumber = 5
elif month == "June":
    monthnumber = 6
elif month == "July":
    monthnumber = 7
elif month == "August":
    monthnumber = 8
elif month == "September":
    monthnumber = 9
elif month == "October":
    monthnumber = 10
elif month == "November":
    monthnumber = 11
elif month == "December":
    monthnumber = 12

if 1980 <= year <= 1989: 
    dec= "the eighties"
elif 1990 <= year <= 1999:
    dec= "the nineties"
elif year < 1980:
    dec= "the stone age"

if 1 <= monthnumber <= 2: 
    season = "winter"
elif 3 <= monthnumber <= 5:
    season = "spring"
elif 6 <= monthnumber <= 8:
    season = "summer"
elif 9 <= monthnumber <= 11:
    season = "fall"
elif monthnumber ==12:
        season = "fall" 
"""
Remember to put in Halloween
"""
if month == "October" and day == 31:
    print(+name+ ", you were born on Halloween.")

print(name+", you are a "+season+" baby of the "+dec+".")




