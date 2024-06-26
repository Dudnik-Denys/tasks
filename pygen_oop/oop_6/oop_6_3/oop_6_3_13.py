def print_file_content(filename: str):
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл не найден')
