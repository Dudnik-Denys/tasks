from calendar import month_name

try:
    n = int(input())
    if n in range(1, 13):
        print(month_name[n])
    else:
        raise IndexError
except IndexError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
