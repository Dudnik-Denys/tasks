from time import monotonic


class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = None
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = monotonic()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = monotonic() - self.start
        self.runs.append(self.end)
        self.last_run, self.min, self.max = self.runs[-1], min(self.runs), max(self.runs)
