class Queue:
    def __init__(self, pairs=None):
        self.pairs = dict(pairs) if pairs else {}

    def add(self, data: tuple):
        data_key, data_value = data
        if data_key not in self.pairs:
            self.pairs[data_key] = data_value
        else:
            self.pairs.pop(data_key)
            self.pairs[data_key] = data_value

    def pop(self):
        if self.pairs:
            key = next(iter(self.pairs))
            value = self.pairs[key]
            del self.pairs[key]
            return key, value
        raise KeyError('Очередь пуста')

    def __repr__(self):
        return f'Queue({[(key, value) for key, value in self.pairs.items()]})'

    def __len__(self):
        return len(self.pairs)
