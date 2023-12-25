class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self, x):
        return sum([self.a * x ** 2, self.b * x, self.c])
