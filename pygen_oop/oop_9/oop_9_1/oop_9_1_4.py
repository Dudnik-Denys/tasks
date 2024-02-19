from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start, step):
        self._current = start
        self._step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current += self._step
        return answer


class GeometricProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current *= self._step
        return answer
