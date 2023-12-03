class Xrange:
    def __init__(self, start, end, step=1):
        self.end = end
        self.step = step
        self.start = start
        self.iterable = []

        if self.step > 0:
            while self.start < self.end:
                self.iterable.append(self.start)
                self.start += self.step
        else:
            while self.start > self.end:
                self.iterable.append(self.start)
                self.start -= abs(self.step)

        self.iterable = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)
