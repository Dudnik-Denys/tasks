def read_csv():
    with open('data.csv', mode='r', encoding='utf-8') as file:
        text = [line.strip().split(',') for line in file.readlines()]
        keys = text[0]
        values = text[1:]
        csv_data = []

        for value in values:
            d = {}
            for i in range(len(keys)):
                d.update({keys[i]: value[i]})
            csv_data.append(d)

    return csv_data


# def read_csv():
#     with open('data.csv') as file:
#         list_of_lines = [line.strip() for line in file.readlines()] # получаем из файла список строк, у каждой из строк обрезаем \n
#     list_of_lists = [line.split(',') for line in list_of_lines]   #преобразуем каждую из строк в список слов
#     list_of_dicts = [dict(zip(list_of_lists[0], list_of_lists[i])) for i in range(1, len(list_of_lists))] #составляем список, каждый элемент которого - словарь, получившийся зипованием нулевого списка и i-того
#     return list_of_dicts

