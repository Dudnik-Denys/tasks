from collections.abc import Sequence


class DNA(Sequence):
    _ELEMENTS = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }

    def __init__(self, chain):
        self._chain = [(elem, self._ELEMENTS[elem]) for elem in chain]

    def __len__(self):
        return len(self._chain)

    def __str__(self):
        return ''.join([pair[0] for pair in self._chain])

    def __contains__(self, item):
        return item in str(self)

    def __getitem__(self, item):
        return self._chain[item]

    def __reversed__(self):
        return reversed(self._chain)

    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(str(self) + str(other))
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, DNA):
            return str(self)[0] == str(other)[0]
        return NotImplemented
