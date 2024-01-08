class SparseArray:
    def __init__(self, default):
        self.default = default
        self.arr = []

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, item):
        try:
            return self.arr[item]
        except IndexError:
            return self.default

    def __setitem__(self, key, value):
        if key in range(len(self.arr)) and len(self.arr):
            self.arr[key] = value
        else:
            new = [self.default] * (key - (len(self.arr) - 1))
            self.arr.extend(new)
            self.arr[key] = value
