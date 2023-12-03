from datetime import datetime, timedelta

dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')


def shop_work_time(data: datetime):
    if data.weekday() <= 4 and 21 > data.hour >= 9:
        return (data.replace(hour=21, minute=0) - data).seconds // 60
    elif data.weekday() > 4 and 18 > data.hour >= 10:
        return (data.replace(hour=18, minute=0) - data).seconds // 60
    return 'Магазин не работает'


print(shop_work_time(dt))
