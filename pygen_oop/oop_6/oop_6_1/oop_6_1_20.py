from typing import Iterable


class Peekable:
    def __init__(self, iterable: Iterable):
        self.iterable = tuple(iterable)
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == len(self.iterable):
            raise StopIteration
        self.__index += 1
        return self.iterable[self.__index - 1]

    def peek(self, default=StopIteration):
        if self.__index == len(self.iterable):
            if default == StopIteration:
                raise StopIteration
            return default

        return self.iterable[self.__index]
