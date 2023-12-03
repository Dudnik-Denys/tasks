from datetime import datetime


def is_available_date(booked_dates: list, date_of_booking: str):
    booked = []
    for d in booked_dates:
        if '-' in d:
            start, finish = d.split('-')
            start, finish = datetime.strptime(start, '%d.%m.%Y').toordinal(), datetime.strptime(finish, '%d.%m.%Y').toordinal()
            for dt in range(start, finish + 1):
                booked.append(dt)
        else:
            booked.append(datetime.strptime(d, '%d.%m.%Y').toordinal())

    for_booked = []

    if '-' in date_of_booking:
        start, finish = date_of_booking.split('-')
        start, finish = datetime.strptime(start, '%d.%m.%Y').toordinal(), datetime.strptime(finish, '%d.%m.%Y').toordinal()
        for dt in range(start, finish + 1):
            for_booked.append(dt)
    else:
        for_booked.append(datetime.strptime(date_of_booking, '%d.%m.%Y').toordinal())

    for dt in for_booked:
        if dt in booked:
            return False
    return True
