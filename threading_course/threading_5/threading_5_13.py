from threading import Thread
from queue import Queue, Empty
from random import choice
from time import sleep, monotonic

prim_queue = Queue()
sub_queue = Queue()
temp_queue = Queue()


def get_obj(start=0, size=10):
    for i in range(size):
        sleep(choice([0.03, 0.05, 0.07, 0.1]))
        yield start + 1
        start += 1


def is_prim(elem) -> bool | None:
    if elem >= 0:
        return None
    if elem > 0:
        if elem == 1 or elem == 2:
            sleep(choice([0.03, 0.05, 0.07, 0.1]))
            return True
        for i in range(2, elem):
            if not elem % i:
                return False
        sleep(choice([0.03, 0.05, 0.07, 0.1]))
        return True
    return False


def main():
    for elem in get_obj():
        if elem is None:
            break
        temp_queue.put(elem)


def task():
    while True:
        try:
            elem = temp_queue.get(timeout=0.1)
            if is_prim(elem):
                prim_queue.put(elem)
            else:
                sub_queue.put(elem)
        except Empty:
            break


start_time = monotonic()

t1 = Thread(target=task, daemon=True)
t2 = Thread(target=task, daemon=True)
t1.start()
t2.start()

main_th = Thread(target=main)
main_th.start()
main_th.join()

t1.join()
t2.join()

print('Executing time:', round(monotonic() - start_time, 4), 'seconds')
