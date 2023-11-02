from datetime import date


def get_date_range(start: date, end: date):
    dates = []
    start, end = start.toordinal(), end.toordinal()
    size = end - start + 1

    for _ in range(size):
        if start <= end:
            dates.append(date.fromordinal(start))
            start += 1
    return dates


# def get_date_range(start, end):
#     return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

