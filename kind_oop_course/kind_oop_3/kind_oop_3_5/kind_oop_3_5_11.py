class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        if isinstance(other, Box):
            return all(elem in other.things for elem in self.things)


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            return self.name.lower() == other.name.lower() and self.mass == other.mass
