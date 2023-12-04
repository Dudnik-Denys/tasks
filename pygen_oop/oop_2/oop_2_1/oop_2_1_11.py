from datetime import date
import calendar

thursdays = 0
now = date(int(input()), int(input()), 1)

for i in range(1, calendar.monthrange(2012, 3)[1] + 1):
    if date(now.year, now.month, i).weekday() == 3:
        thursdays += 1
    if thursdays == 4:
        now = date(now.year, now.month, i)
        break

print(date.strftime(now, '%d.%m.%Y'))
