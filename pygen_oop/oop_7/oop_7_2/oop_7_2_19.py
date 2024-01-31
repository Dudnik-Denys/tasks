class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, value=1):
        self.value += value

    def dec(self, value=1):
        self.value -= value
        if self.value < 0:
            self.value = 0


class DoubledCounter(Counter):
    def inc(self, value=1):
        value *= 2
        super().inc(value)

    def dec(self, value=1):
        value *= 2
        super().dec(value)
