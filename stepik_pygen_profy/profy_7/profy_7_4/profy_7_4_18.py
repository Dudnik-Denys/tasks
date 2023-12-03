import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number: int) -> str:
    try:
        if number > 0:
            return calendar.day_name[number - 1].capitalize()
        else:
            raise IndexError
    except IndexError:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    except TypeError:
        raise TypeError('Аргумент не является целым числом')
