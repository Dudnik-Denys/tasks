try:
    with open(input(), encoding='utf-8') as text_file:
        [print(line.strip()) for line in text_file.readlines()]
except FileNotFoundError:
    print('Файл не найден')
