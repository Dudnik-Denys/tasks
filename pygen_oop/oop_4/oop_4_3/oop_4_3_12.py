class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words.extend(text.split())

    def get_shortest_words(self):
        return list(filter(lambda word: len(word) == len(min(self.words, key=len)), self.words))

    def get_longest_words(self):
        return list(filter(lambda word: len(word) == len(max(self.words, key=len)), self.words))
