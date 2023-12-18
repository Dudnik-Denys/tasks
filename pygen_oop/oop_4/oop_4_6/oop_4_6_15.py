class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def coefficients(self) -> tuple:
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, data: tuple):
        self.a, self.b, self.c = data

    @property
    def x1(self):
        result = (-self.b - (self.discriminant() ** .5)) / (2 * self.a) if self.discriminant() >= 0 else None
        return result

    @property
    def x2(self):
        result = (-self.b + (self.discriminant() ** .5)) / (2 * self.a) if self.discriminant() >= 0 else None
        return result

    def discriminant(self):
        result = (self.b ** 2) - 4 * (self.a * self.c)
        return result

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')
