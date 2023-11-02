from datetime import datetime

dates = [input().split() for _ in range(int(input()))]
dates = {lst[0] + ' ' + lst[1]: datetime.strptime(lst[2], '%d.%m.%Y') for lst in dates}
employees = {}

for employee, dt in dates.items():
    if dt not in employees:
        employees[dt] = [employee]
    else:
        employees[dt].append(employee)

maximum = max({key: len(value) for key, value in employees.items()}.values())
oldest = sorted([key for key, value in employees.items() if len(value) == maximum])
[print(dt.strftime('%d.%m.%Y')) for dt in oldest]
