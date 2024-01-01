class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        result = (self.temperature * 9 / 5) + 32
        return result

    @classmethod
    def from_fahrenheit(cls, fahr):
        result = (5 / 9) * (fahr - 32)
        return cls(result)

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)
