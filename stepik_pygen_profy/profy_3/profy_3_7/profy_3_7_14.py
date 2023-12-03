import calendar
from datetime import date

months = list(calendar.month_name)
data = int(input())


def days_count(year: int, month: str) -> int:
    return calendar.monthrange(year, months.index(month))[1]


def get_third_thursdays(year: int):
    thursdays = []
    count = 0
    for month in range(1, 13):
        for dt in range(1, days_count(year, months[month]) + 1):
            if date(year, month, dt).weekday() == 3:
                count += 1
                if count == 3:
                    thursdays.append(date.strftime(date(year=year, month=month, day=dt), '%d.%m.%Y'))
        count = 0

    [print(thursday) for thursday in thursdays]


get_third_thursdays(data)
