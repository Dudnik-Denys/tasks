from random import choice


class RandomNumber:
    def __init__(self, start: int, end: int, cache: bool = False):
        self.start = start
        self.end= end
        self.cache = cache
        self.first_value = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.cache and self.first_value is not None:
            return self.first_value
        num = choice(range(self.start, self.end + 1))
        self.first_value = num if self.first_value is None else self.first_value
        return num

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')
