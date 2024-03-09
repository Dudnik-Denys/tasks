class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        if isinstance(product, Product):
            self.goods.remove(product)


class Product:
    ID = 1
    ATTRS = {'name': str, 'weight': (int, float), 'price': (int, float)}

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__setattr__('id', cls.ID)
        cls.ID += 1
        return obj

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        del item

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if (key == 'weight' or key == 'price' or key == 'id') and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        if (key == 'weight' or key == 'price' or key == 'id') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)
