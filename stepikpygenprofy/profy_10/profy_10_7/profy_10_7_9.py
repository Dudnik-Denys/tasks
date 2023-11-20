from datetime import date, timedelta


def years_days(year: int):
    current_date = date(year, 1, 1)
    while current_date.year == year:
        yield current_date
        current_date += timedelta(1)
