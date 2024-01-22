class RadiusVector:
    def __init__(self, *coordinates):
        if len(coordinates) == 1:
            self.coordinates = [0 for _ in range(coordinates[0])]
        else:
            self.coordinates = [elem for elem in coordinates]

    def set_coords(self, *coords):
        size = len(coords) if len(coords) <= len(self.coordinates) else len(self.coordinates)

        for i in range(size):
            self.coordinates[i] = coords[i]

    def get_coords(self):
        return self.coordinates

    def __len__(self):
        return len(self.coordinates)

    def __abs__(self):
        return sum([coord ** 2 for coord in self.coordinates]) ** .5
