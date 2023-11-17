class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        self.times -= 1
        if self.times < 0:
            raise StopIteration
        else:
            return self.obj
