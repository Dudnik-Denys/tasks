from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def int_case(obj):
        return -obj

    @neg.register(bool)
    @staticmethod
    def bool_case(obj):
        return not obj
