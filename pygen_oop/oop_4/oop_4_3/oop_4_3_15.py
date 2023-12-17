class Wordplay:
    def __init__(self, words=None):
        self.words = words[:] if words else []

    def add_word(self, word):
        self.words.append(word) if word not in self.words else None

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *letters):
        return [word for word in self.words if all(bool(letter in letters) for letter in word)]

    def avoid(self, *letters):
        return [word for word in self.words if not any(bool(letter in letters) for letter in word)]
