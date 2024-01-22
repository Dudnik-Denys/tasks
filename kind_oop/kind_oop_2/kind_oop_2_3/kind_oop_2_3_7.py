class FloatValue:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        instance.__dict__[self._name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M, start=0.0, increment=1.0):
        self.cells = [[Cell(start := start + increment) for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
