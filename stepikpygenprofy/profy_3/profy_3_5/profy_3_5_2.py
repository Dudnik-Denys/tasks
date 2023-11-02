from datetime import datetime, timedelta

days = [0, 0, 0, 0, 0, 0, 0]

start = datetime(day=1, month=1, year=1)
finish = datetime(day=31, month=12, year=9999)

for _ in range(finish.toordinal() - 1):
    if start.day == 13:
        days[start.weekday()] += 1
    start = start + timedelta(days=1)

[print(dt) for dt in days]
