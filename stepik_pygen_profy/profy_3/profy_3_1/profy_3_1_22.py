from datetime import date


def saturdays_between_two_dates(start: date, end: date):
    start = start.toordinal()
    end = end.toordinal()
    saturday_counter = 0

    if start > end:
        end, start = start, end

    while start <= end:
        if date.fromordinal(start).weekday() == 5:
            saturday_counter += 1
        start += 1

    return saturday_counter


# def saturdays_between_two_dates(start, end):
#     if start > end:
#         start, end = end, start
#
#     return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1))
