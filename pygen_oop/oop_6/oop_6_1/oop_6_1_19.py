from random import choice


class RandomLooper:
    def __init__(self, *iterables):
        self.common = []
        for iterable in iterables:
            self.common.extend(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        length = len(self.common)
        sequence = range(length)

        if length > 0:
            random_index = choice(sequence)
            return self.common.pop(random_index)
        raise StopIteration
