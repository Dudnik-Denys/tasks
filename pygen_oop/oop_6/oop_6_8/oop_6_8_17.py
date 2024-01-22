class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self.times = times

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.times == 0:
            raise MaxCallsException('Превышено количество доступных обращений')
        if self._name in instance.__dict__:
            self.times -= 1
            return instance.__dict__[self._name]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
