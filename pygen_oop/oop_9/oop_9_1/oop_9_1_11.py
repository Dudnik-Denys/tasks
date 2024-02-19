class Currency:
    _RATES = {
        'EUR': 1,
        'RUB': 90,
        'USD': 1.1,
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{round(float(self.amount), 2)} {self.currency}"

    def __add__(self, other):
        other.change_to(self.currency)
        return Currency(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        other.change_to(self.currency)
        return Currency(self.amount - other.amount, self.currency)

    def __mul__(self, other):
        other.change_to(self.currency)
        amount = self.amount * other.amount
        return Currency(amount, self.currency)

    def __truediv__(self, other):
        other.change_to(self.currency)
        amount = self.amount / other.amount
        return Currency(amount, self.currency)

    @classmethod
    def _rate(cls, current, desired):
        return cls._RATES[desired] / cls._RATES[current]

    def change_to(self, currency):
        rate = self._rate(self.currency, currency)
        self.amount *= rate
        self.currency = currency
