import calendar

months = list(calendar.month_abbr)
data = input().split()

print(calendar.month(int(data[0]), months.index(data[1])))
