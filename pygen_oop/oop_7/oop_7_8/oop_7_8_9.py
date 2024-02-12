class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, radius: int, center: Point):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'({self.center.x}, {self.center.y}), r = {self.radius}'
