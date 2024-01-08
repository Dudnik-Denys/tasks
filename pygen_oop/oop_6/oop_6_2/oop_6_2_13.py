from copy import deepcopy


class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = deepcopy(sequences)

    def __len__(self):
        return min((len(s) for s in self.sequences), default=0)

    def __getitem__(self, index):
        count = -1
        for item in self:
            count += 1
            if count == index:
                return item

    def __iter__(self):
        yield from zip(*self.sequences)
