class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter: int | float):
        return Circle(diameter / 2)
