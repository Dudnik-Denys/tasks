class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if isinstance(thing, Thing) and thing.weight <= (self.max_weight - self.get_total_weight()):
            self.__things.append(thing)

    def remove_thing(self, index):
        self.__things.pop(index)

    def get_total_weight(self):
        return sum(thing.weight for thing in self.__things) if self.__things else 0


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if type(weight) in (int, float):
            self._weight = weight
