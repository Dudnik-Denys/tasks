from queue import Queue

first_queue = Queue()
second_queue = Queue()

for i in range(10):
    first_queue.put(i)

n = first_queue.qsize()

for i in range(n):
    elem = first_queue.get()
    second_queue.put(elem)
