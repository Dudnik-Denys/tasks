from datetime import datetime

data = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]


def date_next_door(dates: list) -> list:
    difference = []
    if len(dates) > 1:
        difference = [abs((dates[x] - dates[x - 1]).days) for x in range(1, len(dates))]
        return difference
    return difference


print(date_next_door(data))

# from datetime import date, time, timedelta, datetime
#
# dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]
#
# diffs = [abs(dates[i] - dates[i - 1]).days for i in range(1, len(dates))]
#
# print(diffs)
