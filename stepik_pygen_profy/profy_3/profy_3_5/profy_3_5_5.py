from datetime import datetime

dates = [input().split() for _ in range(int(input()))]
dates = {lst[0] + ' ' + lst[1]: datetime.strptime(lst[2], '%d.%m.%Y') for lst in dates}
employees = {}

for employee, dt in dates.items():
    if dt not in employees:
        employees[dt] = [employee]
    else:
        employees[dt].append(employee)

minimal_date = min(employees)

if len(employees[minimal_date]) > 1:
    print(minimal_date.strftime('%d.%m.%Y'), len(employees[minimal_date]))
else:
    print(minimal_date.strftime('%d.%m.%Y'), *employees[minimal_date])
