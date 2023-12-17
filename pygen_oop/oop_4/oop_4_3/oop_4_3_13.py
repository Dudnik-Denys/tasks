class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, n):
        return [thing for thing, priority in self.things if priority == n]

    def get_low_priority(self):
        priority = min(self.things, key=lambda x: x[1])[1]
        return self.get_by_priority(priority)

    def get_high_priority(self):
        priority = max(self.things, key=lambda x: x[1])[1]
        return self.get_by_priority(priority)
