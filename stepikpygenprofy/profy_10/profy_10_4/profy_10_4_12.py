class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = zip(data.keys(), data.values())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)
