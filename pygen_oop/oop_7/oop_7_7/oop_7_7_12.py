from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=None):
        self.iterable = iterable[:] if iterable else []

    def add(self, num):
        if type(num) in (int, float):
            self.iterable.append(num)

    def clear(self):
        self.iterable.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        return min(self.iterable) if self.iterable else None


class MaxStat(Stat):
    def result(self):
        return max(self.iterable) if self.iterable else None


class AverageStat(Stat):
    def result(self):
        return sum(self.iterable) / len(self.iterable) if self.iterable else None
