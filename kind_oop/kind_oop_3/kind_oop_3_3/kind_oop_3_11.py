class PolyLine:
    def __init__(self, *coordinates):
        self.coordinates = list(coordinates)

    def add_coord(self, x, y):
        self.coordinates.append((x, y))

    def remove_coord(self, index):
        self.coordinates.pop(index)

    def get_coords(self):
        return self.coordinates
