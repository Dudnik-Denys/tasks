class Validator:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self._name] = value

    def validate(self, obj):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if type(obj) not in (int, float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None and obj < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue is not None and obj > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize is not None and len(obj) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize is not None and len(obj) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is not None and not self.predicate(obj):
            raise ValueError(f'Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True
