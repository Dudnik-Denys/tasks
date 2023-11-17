from datetime import date, timedelta


def dates(start: date, count: int | None = None):
    index = 0
    while index != count:
        try:
            yield start
            start += timedelta(1)
            index += 1
        except OverflowError:
            return StopIteration
