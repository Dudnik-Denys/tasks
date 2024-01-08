from collections import OrderedDict


class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        return f"Row({', '.join([f'{key}={repr(value)}' for key, value in self.__dict__.items()])})"

    def __eq__(self, other):
        if isinstance(other, Row):
            return OrderedDict(self.__dict__) == OrderedDict(other.__dict__)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Row):
            return OrderedDict(self.__dict__) != OrderedDict(other.__dict__)
        return NotImplemented

    def __hash__(self):
        return sum(hash(key) for key in enumerate(self.__dict__, 1))
