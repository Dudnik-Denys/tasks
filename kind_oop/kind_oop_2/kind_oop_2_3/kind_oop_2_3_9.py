class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        if isinstance(product, Product) and product in self.goods:
            self.goods.remove(product)


class StringValue:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if isinstance(value, str) and 2 <= len(value) <= 50:
            instance.__dict__[self._name] = value


class PriceValue:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if type(value) in (int, value) and 0 <= value <= 10_000:
            instance.__dict__[self._name] = value


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price
