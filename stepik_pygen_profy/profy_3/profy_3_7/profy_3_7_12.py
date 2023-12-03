import calendar
from datetime import date

months = list(calendar.month_name)


def days_count(year: int, month: str):
    return calendar.monthrange(year, months.index(month))[1]


def get_days_in_month(year: int, month: str):
    dates = []
    for dt in range(1, days_count(year, month) + 1):
        dates.append(date(year, months.index(month), dt))
    return dates
