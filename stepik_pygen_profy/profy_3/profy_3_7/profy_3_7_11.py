import calendar

year, month = input().split()
months = list(calendar.month_name)
print(calendar.monthrange(int(year), months.index(month))[1])
