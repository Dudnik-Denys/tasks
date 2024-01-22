class TypeChecked:
    def __init__(self, *types):
        self.types = types

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if type(value) not in self.types:
            raise TypeError('Некорректное значение')
        instance.__dict__[self._name] = value
