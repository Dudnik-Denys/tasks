from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def int_case(obj):
        print(f'Целое число: {obj}')

    @format.register(float)
    @staticmethod
    def float_case(obj):
        print(f'Вещественное число: {obj}')

    @format.register(list)
    @staticmethod
    def list_case(obj):
        print(f'Элементы списка: {", ".join(map(str, obj))}')

    @format.register(tuple)
    @staticmethod
    def tuple_case(obj):
        print(f'Элементы кортежа: {", ".join(map(str, obj))}')

    @format.register(dict)
    @staticmethod
    def dict_case(obj):
        print(f'Пары словаря: {", ".join(map(str, obj.items()))}')
