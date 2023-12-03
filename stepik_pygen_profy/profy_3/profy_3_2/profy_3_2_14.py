from datetime import date


def print_good_dates(dates: list[date]):
    for d in sorted(dates):
        if d.year == 1992 and d.month + d.day == 29:
            print(d.strftime('%B %d, %Y'))
