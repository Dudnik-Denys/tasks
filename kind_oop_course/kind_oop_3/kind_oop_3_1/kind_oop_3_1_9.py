class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __getattr__(self, item):
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (int, float):
            self.__x = x
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if type(radius) in (int, float) and radius > 0:
            self.__radius = radius
