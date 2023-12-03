import json

try:
    with open(input(), encoding='utf_8') as json_file:
        try:
            json.load(json_file)
        except json.JSONDecodeError:
            print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')
