class PowerOf:
    def __init__(self, number):
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.number ** self.index
