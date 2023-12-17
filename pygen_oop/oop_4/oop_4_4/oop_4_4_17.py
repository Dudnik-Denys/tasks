from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = pi * (self._radius ** 2)

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area
