from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self._diapasons = []
        for diapason in args:
            if isinstance(diapason, int):
                self._diapasons.append(diapason)
            if isinstance(diapason, str):
                start, finish = map(int, diapason.split('-'))
                self._diapasons.extend(range(start, finish + 1))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._diapasons[item]
        return NotImplemented

    def __len__(self):
        return len(self._diapasons)
