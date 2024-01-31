class Budget:
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it)

    def remove_item(self, index):
        self.budget.pop(index)

    def get_items(self):
        return self.budget


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        if isinstance(other, int) or isinstance(other, float):
            return self.money + other

    def __radd__(self, other):
        return self.__add__(other)
