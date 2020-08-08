months = {
    'January' : 31,
    'February' : 28,
    'March' : 31,
    'April' : 30,
    'May' : 31,
    'June' : 30,
    'July' : 31,
    'August' : 31,
    'September' : 30,
    'October' : 31,
    'November' : 30,
    'December': 31
    }

def isLeapYear(year):return (year%400 == 0) or (year%4 == 0 and year%100!=0)

month, day, year, time = input().split()
day, year, hour, minute = map(int,[day[:-1], year]+time.split(':'))

yearSec = 366 if isLeapYear(year) else 365
yearSec *= 60*60*24

passedSec = 0
for key,val in months.items():
    if key==month:break
    elif key=='February' and isLeapYear(year): passedSec += 29
    else:passedSec += val
passedSec += day - 1
passedSec *= 60*60*24
passedSec += hour*3600 + minute*60

print(passedSec/yearSec*100)
