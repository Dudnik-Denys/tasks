from queue import PriorityQueue


class CCD:
    def __init__(self, cargo_details=None):
        self._cargo_details = {} if cargo_details is None else cargo_details
        self.cat, self.union, self.cargo, self.id = self._cargo_details.values()

    def __lt__(self, other):
        if isinstance(other, CCD):
            if self.union != other.union:
                return self.union > other.union
            elif int(self.cat) in range(201, 210) and int(other.cat) not in range(201, 210):
                return True
            elif int(self.cat) not in range(201, 210) and int(other.cat) in range(201, 210):
                return False
            else:
                return self.id < other.id
        return NotImplemented

    def __repr__(self):
        return f'{type(self).__name__}({repr(self._cargo_details)})'


pq = PriorityQueue()
data = [
    {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1},
    {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2},
    {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3},
    {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4},
    {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5},
    {"cat": "0201", "union": False, "cargo": {"veal", 120}, "id": 7},
    {"cat": "0201", "union": False, "cargo": {"veal", 79}, "id": 6}
    ]

for elem in data:
    pq.put(CCD(elem))

size = pq.qsize()

for _ in range(size):
    obj = pq.get()
    print(obj)
