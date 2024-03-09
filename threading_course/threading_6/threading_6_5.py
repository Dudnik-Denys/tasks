from queue import PriorityQueue, Full
from threading import Thread


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


def handler(declaration):
    return declaration is not None


def get_next_declar():
    yield from iter(declarations)


def main():
    for elem in get_next_declar():
        if elem is None:
            break
        try:
            main_queue.put_nowait(CCD(elem))
        except Full:
            sup_queue.put(CCD(elem))


def task():
    while not main_queue.empty():
        elem = main_queue.get()
        handler(elem)
        main_queue.task_done()


main_queue = PriorityQueue(30)
sup_queue = PriorityQueue()

declarations = [
    {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1},
    {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2},
    {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3},
    {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4},
    {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5},
    {"cat": "0201", "union": False, "cargo": {"veal", 120}, "id": 7},
    {"cat": "0201", "union": False, "cargo": {"veal", 79}, "id": 6},
    {"cat": "0210", "union": True, "cargo": {"stew", 5}, "id": 8},
    {"cat": "0208", "union": True, "cargo": {"liver", 2.13}, "id": 9},
    {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 10},
    {"cat": "0209", "union": False, "cargo": {"pork fat", 90}, "id": 13},
    {"cat": "87", "union": True, "cargo": {"bombardier", 3}, "id": 14},
    {"cat": "0201", "union": False, "cargo": {"veal", 134}, "id": 11},
    {"cat": "0201", "union": False, "cargo": {"veal", 80}, "id": 12},
    {"cat": "0210", "union": False, "cargo": {"stew", 3}, "id": 15},
    {"cat": "0208", "union": False, "cargo": {"liver", 1.78}, "id": 21},
    {"cat": "0208", "union": False, "cargo": {"liver", 56}, "id": 23},
    {"cat": "0209", "union": False, "cargo": {"pork fat", 85}, "id": 16},
    {"cat": "87", "union": False, "cargo": {"bombardier", 2}, "id": 27},
    {"cat": "0201", "union": False, "cargo": {"veal", 120}, "id": 24},
    {"cat": "0201", "union": False, "cargo": {"veal", 79}, "id": 17},
    {"cat": "0210", "union": True, "cargo": {"stew", 5}, "id": 19},
    {"cat": "0208", "union": True, "cargo": {"liver", 0.99}, "id": 20},
    {"cat": "0208", "union": False, "cargo": {"liver", 41}, "id": 18},
    {"cat": "0209", "union": False, "cargo": {"pork fat", 123}, "id": 26},
    {"cat": "87", "union": True, "cargo": {"bombardier", 4}, "id": 25},
    {"cat": "0201", "union": True, "cargo": {"veal", 181}, "id": 21},
    {"cat": "0201", "union": False, "cargo": {"veal", 99}, "id": 28},
    {"cat": "0208", "union": True, "cargo": {"liver", 0.76}, "id": 33},
    {"cat": "0208", "union": True, "cargo": {"liver", 35}, "id": 31},
    {"cat": "0209", "union": False, "cargo": {"pork fat", 60}, "id": 29},
    {"cat": "87", "union": True, "cargo": {"bombardier", 2}, "id": 32},
    {"cat": "0201", "union": True, "cargo": {"veal", 90}, "id": 34},
    {"cat": "0201", "union": True, "cargo": {"veal", 82}, "id": 30},
    None
    ]

prod_0 = Thread(target=main, name='prod_0')
insp_1 = Thread(target=task, name='insp_1', daemon=True)
insp_2 = Thread(target=task, name='insp_2', daemon=True)
insp_3 = Thread(target=task, name='insp_3', daemon=True)

prod_0.start()
prod_0.join()

insp_1.start()
insp_2.start()
insp_3.start()

main_queue.join()

while not sup_queue.empty():
    elem = sup_queue.get()
    main_queue.put(elem)

for _ in range(main_queue.qsize()):
    print(main_queue.get())
