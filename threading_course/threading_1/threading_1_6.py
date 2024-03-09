import threading


def my_task(x):
    return x


def my_new_task(x):
    return x


tasks = [my_task, my_new_task]
args = [1, 2]

for i in range(len(tasks)):
    threading.Thread(target=tasks[i], args=(args[i],), name=tasks[i].__name__).start()
