class HighScoreTable:
    def __init__(self, length: int):
        self._length = length
        self.scores = []

    def update(self, value: int):
        if not self.scores and self._length >= 1:
            self.scores.append(value)
        elif value >= min(self.scores) or len(self.scores) < self._length:
            self.scores.append(value)
            self.scores = sorted(self.scores, reverse=True)
            if len(self.scores) > self._length:
                self.scores.pop()

    def reset(self):
        self.scores = []
