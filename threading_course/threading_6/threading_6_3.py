from queue import Queue
from threading import Thread

valid_queue = Queue()
none_valid_queue = Queue()


def task():
    while True:
        elem = valid_queue.get()
        if elem is None:
            valid_queue.put(elem)
            break
        handler(elem)


t1 = Thread(target=task, daemon=True)
t2 = Thread(target=task, daemon=True)
t1.start()
t2.start()


def main():
    for elem in get_obj():
        if elem is not None:
            if is_valid(elem):
                valid_queue.put(elem)
            else:
                none_valid_queue.put(elem)
        else:
            valid_queue.put(elem)
            break


main_th = Thread(target=main)
main_th.start()
main_th.join()
t1.join()
t2.join()
