import threading
import time
import random
from typing import Callable


def finalizer():
    print("STAGE #1 ALL DONE!")


def task_st_1():
    time.sleep(random.uniform(0, 1))
    print(f"stage #1 done by {threading.current_thread().name}")


def task_st_2():
    time.sleep(random.uniform(0, 1))
    print(f"stage #2 done by {threading.current_thread().name}")


# Создайте объект барьера
barrier = threading.Barrier(4, timeout=1, action=finalizer)


# Создайте целевую функцию, выполняющую задачи в два этапа
def main(bar: threading.Barrier, func_1: Callable, func_2: Callable):
    func_1()
    bar.wait()
    func_2()


# Создайте и запустите 4 потока
threads = [threading.Thread(target=main, args=(barrier, task_st_1, task_st_2)).start() for _ in range(4)]
