class Queue:
    def __init__(self, *args):
        self.queue = [*args]

    def add(self, *args):
        self.queue.extend(args)

    def pop(self):
        return self.queue.pop(0) if self.queue else None

    def __str__(self):
        return ' -> '.join(map(str, self.queue))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.queue == other.queue
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.queue + other.queue))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.add(*other.queue)
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            return Queue(*self.queue[n:])
        return NotImplemented
