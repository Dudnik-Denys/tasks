from datetime import datetime
from stepikpygenprofy.profy_2.profy_2_1.profy_2_1_14 import choose_plural

release = datetime(2022, 11, 8, 12)
date_now = datetime.strptime(input(), '%d.%m.%Y %H:%M')
difference = release - date_now
diff_hours = difference.seconds // 3600
diff_minutes = (difference.seconds // 60) % 60

message = 'До выхода курса осталось:'

if date_now < release:
    if difference.days > 0 and diff_hours > 0:
        message += ' ' + choose_plural(difference.days, ('день', 'дня', 'дней'))
        message += ' и ' + choose_plural(diff_hours, ('час', 'часа', 'часов'))
    elif difference.days > 0 and diff_hours <= 0:
        message += ' ' + choose_plural(difference.days, ('день', 'дня', 'дней'))
    elif diff_hours > 0 and difference.days <= 0 and diff_minutes <= 0:
        message += ' ' + choose_plural(diff_hours, ('час', 'часа', 'часов'))
    elif diff_hours > 0 and difference.days <= 0 and diff_minutes > 0:
        message += ' ' + choose_plural(diff_hours, ('час', 'часа', 'часов'))
        message += ' и ' + choose_plural(diff_minutes, ('минута', 'минуты', 'минут'))
    elif diff_minutes > 0 and diff_hours <= 0 and difference.days <= 0:
        message += ' ' + choose_plural(diff_minutes, ('минута', 'минуты', 'минут'))
    print(message)
else:
    print('Курс уже вышел!')
