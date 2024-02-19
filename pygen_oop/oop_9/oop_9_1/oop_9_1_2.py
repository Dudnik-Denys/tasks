from math import sqrt


class Vector:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return f'{self.coordinates}'

    def __add__(self, other):
        if isinstance(other, Vector) and len(other.coordinates) == len(self.coordinates):
            return Vector(*[self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates))])
        raise ValueError('Векторы должны иметь равную длину')

    def __sub__(self, other):
        if isinstance(other, Vector) and len(other.coordinates) == len(self.coordinates):
            return Vector(*[self.coordinates[i] - other.coordinates[i] for i in range(len(self.coordinates))])
        raise ValueError('Векторы должны иметь равную длину')

    def __mul__(self, other):
        if isinstance(other, Vector) and len(other.coordinates) == len(self.coordinates):
            return sum([self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates))])
        raise ValueError('Векторы должны иметь равную длину')

    def norm(self):
        return sqrt(sum(x ** 2 for x in self.coordinates))

    def __eq__(self, other):
        if isinstance(other, Vector) and len(other.coordinates) == len(self.coordinates):
            return self.coordinates == other.coordinates
        raise ValueError('Векторы должны иметь равную длину')
