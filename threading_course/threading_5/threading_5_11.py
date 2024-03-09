from queue import Queue

prim_queue = Queue()
sub_queue = Queue()


def get_obj(start=0, size=10):
    for i in range(size):
        yield start + 1
        start += 1


def is_prim(elem):
    if elem > 0:
        if elem == 1 or elem == 2:
            return True
        for i in range(2, elem):
            if not elem % i:
                return False
        return True
    return False


[prim_queue.put(x) if is_prim(x) else sub_queue.put(x) for x in get_obj()]
