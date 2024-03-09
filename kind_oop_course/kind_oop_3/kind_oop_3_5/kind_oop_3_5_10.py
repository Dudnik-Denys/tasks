from functools import total_ordering


@total_ordering
class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.get_weight() == other.get_weight()
        if type(other) in (int, float):
            return self.get_weight() == other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.get_weight() < other.get_weight()
        if type(other) in (int, float):
            return self.get_weight() < other
