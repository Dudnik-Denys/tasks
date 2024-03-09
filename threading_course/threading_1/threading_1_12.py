import threading
from time import monotonic, sleep


def my_task(a=2):
    print(threading.current_thread())
    sleep(a)


def my_new_task(b=2):
    print(threading.current_thread())
    sleep(b)


tasks = [my_task, my_new_task, my_task, my_new_task, my_task, my_new_task, my_task, my_new_task, my_task, my_new_task,]
kwargs = [{'a': 1}, {'b': 1}, {'a': 1}, {'b': 1}, {'a': 1}, {'b': 1}, {'a': 1}, {'b': 1}, {'a': 1}, {'b': 1}]


threads = []
start = monotonic()
print(f'Start time: {start}')

for i in range(len(tasks)):
    t = threading.Thread(target=tasks[i], kwargs=kwargs[i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
