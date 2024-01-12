from contextlib import contextmanager


@contextmanager
def safe_write(filename: str):
    try:
        result = open(filename, 'r', encoding='UTF-8')
        result.close()
    except FileNotFoundError:
        result = open(filename, 'w', encoding='UTF-8')
        result.close()
    result = open(filename, 'r+', encoding='UTF-8')
    flag = False

    try:
        draft = open('draft.txt', 'w', encoding='UTF-8')
        yield draft
    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {type(error).__name__}')
        flag = True
    finally:
        if not flag:
            draft.close()
            temp = open(draft.name, 'r', encoding='UTF-8')
            result.write(temp.read())
            temp.close()
            result.close()


# from contextlib import contextmanager
#
#
# @contextmanager
# def safe_write(filename):
#     file = open(filename, 'a', encoding='u8')
#     cursor = file.tell()
#     try:
#         yield file
#     except Exception as err:
#         file.truncate(cursor)
#         print('Во время записи в файл было возбуждено исключение', type(err).__name__)
#     finally:
#         file.close()
