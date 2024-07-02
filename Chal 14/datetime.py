import datetime
date = datetime.date.today()
print(date)


#each date information separately:

day = datetime.date.today().day
month = datetime.date.today().month
year = datetime.date.today().year

print(day)
print(month)
print(year)

#Time formatting
format1 = now.strftime('%d/%m/%y')
print(format1)

format2 = now.strftime('%d.%m.%Y %H:%M:%S')
print(format2)
