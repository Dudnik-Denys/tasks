class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self._real = value

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self._img = value

    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** .5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
