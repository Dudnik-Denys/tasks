class WordString:
    def __init__(self, string=''):
        self.string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    def __len__(self):
        return len(self._string.split())

    def __call__(self, index):
        return self._string.split()[index]
