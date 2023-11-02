from datetime import datetime, timedelta


def difference_dates(dt1: datetime, dt2: datetime) -> int:
    difference = abs(dt2 - dt1).days
    return difference


def fill_up_missing_dates(data: list[str]) -> list:
    missed_dates = []
    data = sorted([datetime.strptime(d, '%d.%m.%Y') for d in data])
    for i in range(1, len(data)):
        diff = difference_dates(data[i - 1], data[i])
        if diff > 1:
            for x in range(diff - 1):
                dt = data[i - 1] + timedelta(days=x + 1)
                missed_dates.append(dt)

    data = data + missed_dates
    data = sorted([dt.strftime('%d.%m.%Y') for dt in data])

    return data
