class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        if type(item) == int:
            return self.sequence[-item - 1]
