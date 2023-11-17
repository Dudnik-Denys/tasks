from random import choice


class InfinityRandom:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        self.sequence = list(range(start, finish + 1))

    def __iter__(self):
        return self

    def __next__(self):
        return choice(self.sequence)


def random_numbers(left: int, right: int) -> iter:
    inf = InfinityRandom(left, right)
    return inf
