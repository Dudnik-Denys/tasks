class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
coordinates = (1, 1)

for _ in range(1000):
    x, y = coordinates
    point = Point(*coordinates)
    points.append(point)
    coordinates = (x + 2, y + 2)

points[1].color = 'yellow'
