class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, value=1):
        self.value += value

    def dec(self, value=1):
        self.value -= value
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, value=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, value=1):
        self.value += value
        if self.value > self.limit:
            self.value = self.limit
