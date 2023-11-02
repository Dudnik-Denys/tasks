from datetime import datetime, timedelta

birthday = datetime.strptime(input(), '%d.%m.%Y')
birthdays = [birthday + timedelta(days=i) for i in range(1, 8)]
dates = [input().split() for _ in range(int(input()))]
dates = {datetime.strptime(lst[2], '%d.%m.%Y'): lst[0] + ' ' + lst[1] for lst in dates}
minimal = datetime(day=31, month=12, year=1)

for dt, employee in dates.items():
    for d in birthdays:
        if dt.day == d.day and dt.month == d.month and dt.year > minimal.year:
            minimal = dt

if minimal.year > 1:
    print(dates[minimal])
else:
    print('Дни рождения не планируются')
