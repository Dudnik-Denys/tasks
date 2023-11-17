from random import randint


class RandomNumbers:
    def __init__(self, left: int, right: int, n: int):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return randint(self.left, self.right)
        raise StopIteration
