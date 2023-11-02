import calendar
from datetime import date

months = list(calendar.month_name)


def days_count(year: int, month: str) -> int:
    return calendar.monthrange(year, months.index(month))[1]


def get_all_mondays(year: int) -> list:
    mondays = []
    for month in range(1, 13):
        for dt in range(1, days_count(year, months[month]) + 1):
            if date(year, month, dt).weekday() == 0:
                mondays.append(date(year, month, dt))
    return mondays
