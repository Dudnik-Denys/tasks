class AttrsIterator:
    def __init__(self, obj):
        self.arr = [(key, value) for key, value in obj.__dict__.items()]
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == len(self.arr):
            raise StopIteration
        self.__index += 1
        return self.arr[self.__index - 1]
