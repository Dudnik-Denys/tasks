class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y})'

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'
