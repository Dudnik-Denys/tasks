from typing import Iterable, Any


class CyclicList:
    def __init__(self, iterable: Iterable = []):
        self.iterable = list(iterable)

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, item: int):
        return self.iterable[item % (len(self.iterable))]

    def append(self, item: Any):
        self.iterable.append(item)

    def pop(self, index: int = -1):
        return self.iterable.pop(index)
