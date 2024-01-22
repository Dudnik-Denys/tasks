class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__ and self._default is not None:
            return self._default
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        raise AttributeError('Аттрибут не найден')

    def __set__(self, instance, value):
        if type(value) == int and value >= 0:
            instance.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')
