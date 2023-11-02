from datetime import date


dates = []
while (data := input()) != 'end':
    dates.append(data)


def is_correct(lst):
    counter = 0
    for d in lst:
        try:
            d = d.split('.')
            date(int(d[2]), int(d[1]), int(d[0]))
            counter += 1
            print('Корректная')
        except:
            print('Некорректная')
    print(counter)


is_correct(dates)
