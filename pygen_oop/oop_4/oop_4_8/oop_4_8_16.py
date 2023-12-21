from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def int_float_processor(obj):
        return obj * 2

    @process.register(str)
    @staticmethod
    def int_float_processor(obj):
        return obj.upper()

    @process.register(list)
    @staticmethod
    def int_float_processor(obj):
        return sorted(obj)

    @process.register(tuple)
    @staticmethod
    def int_float_processor(obj):
        return tuple(sorted(obj))
