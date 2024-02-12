class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=None):
        self.items = items[:] if items else []

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)

    def add(self, item: Item):
        self.items.append(item)

    def remove(self, name: str):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)

    def total(self):
        return sum(item.price for item in self.items)
