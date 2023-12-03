from datetime import date


def get_min_max(dates: list[date]):
    if dates:
        return min(dates), max(dates)
    return ()
