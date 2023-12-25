from typing import Iterable, Callable


class Filter:
    def __init__(self, predicate: Callable):
        self.predicate = bool if predicate is None else predicate

    def __call__(self, iterable: Iterable) -> list:
        return [elem for elem in iterable if self.predicate(elem)]
