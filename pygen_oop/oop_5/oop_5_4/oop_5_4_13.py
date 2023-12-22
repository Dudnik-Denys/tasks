class ColoredPoint:
    def __init__(self, x: int, y: int, color: tuple = (0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, data: tuple):
        if all(256 > num > -1 for num in data):
            self._color = data

    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y}, {self._color})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self._color)

    def __neg__(self):
        return ColoredPoint(self.x * -1, self.y * -1, self._color)

    def __invert__(self):
        r, g, b = self._color
        return ColoredPoint(self.y, self.x, (255 - r, 255 - g, 255 - b))
