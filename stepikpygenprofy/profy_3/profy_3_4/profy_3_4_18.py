from datetime import datetime


def num_of_sundays(year: int) -> int:
    dt1 = datetime(year=year, month=1, day=1).toordinal()
    dt2 = datetime(year=year + 1, month=1, day=1).toordinal()
    sundays = [dt for dt in range(dt1, dt2) if datetime.fromordinal(dt).weekday() == 6]
    return len(sundays)


# from datetime import date
#
# def num_of_sundays(year: int) -> int:
#     return 52 if date(year, 12, 31).strftime('%w') != '0' else 53
