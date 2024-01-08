from typing import Iterable


class SkipIterator:
    def __init__(self, iterable: Iterable, n: int):
        self.iterable = tuple(iterable)
        self.n = n
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1 if self.__index == 0 else (1 + self.n)

        if self.__index > len(self.iterable):
            raise StopIteration
        if self.__index == 1:
            return self.iterable[self.__index - 1]
        return self.iterable[self.__index - 1]
