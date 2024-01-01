class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        self.__dict__[key] = value

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')
