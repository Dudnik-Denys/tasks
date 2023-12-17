class Numbers:
    def __init__(self):
        self.numbers = ()

    def add_number(self, num):
        self.numbers += (num, )

    def get_even(self):
        return list(filter(lambda x: not x % 2, self.numbers))

    def get_odd(self):
        return list(filter(lambda x: x % 2, self.numbers))
