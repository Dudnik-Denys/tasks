class Square:
    def __init__(self, n):
        self.sequence = n

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, number):
        self._sequence = (num for num in range(1, number + 1))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._sequence)
