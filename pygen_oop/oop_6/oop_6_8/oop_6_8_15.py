from keyword import kwlist


class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._attr in instance.__dict__:
            return instance.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        instance.__dict__[self._attr] = value
