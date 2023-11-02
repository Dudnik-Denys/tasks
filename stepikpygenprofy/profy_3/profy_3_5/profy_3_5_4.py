from datetime import datetime

start, finish = datetime.strptime(input(), '%d.%m.%Y'), datetime.strptime(input(), '%d.%m.%Y')

dates = [datetime.fromordinal(dt) for dt in range(start.toordinal(), finish.toordinal() + 1)]

for dt in dates:
    if (dt.month + dt.day) % 2 != 0:
        start = dt
        break

dates = dates[dates.index(start)::3]

for dt in dates:
    if dt.weekday() not in [0, 3]:
        print(dt.strftime('%d.%m.%Y'))
