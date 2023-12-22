from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word: str):
        self.word = word

    def __repr__(self):
        return f"{type(self).__name__}('{self.word}')"

    def __str__(self):
        return self.word.title()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        if isinstance(other, str):
            return len(self.word) == len(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        if isinstance(other, str):
            return len(self.word) > len(other)
        return NotImplemented
