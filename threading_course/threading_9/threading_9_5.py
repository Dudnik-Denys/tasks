import threading
from typing import Callable
from functools import wraps
from time import sleep


def func_test():
    print(f'{threading.current_thread().name} executing before sleep')
    sleep(1)
    print(f'{threading.current_thread().name} executing after sleep')


# допишите код
class HubHendler:
    def __init__(self, n: int, task: Callable, n_threads: int):
        self.n = n
        self.task = self._executor(task)
        self.n_threads = n_threads
        self.semaphore = threading.Semaphore(self.n)

    def start_hub(self):
        threads = [threading.Thread(target=self._executor, args=(self.task, )) for _ in range(self.n_threads)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    # при необходимости используйте дополнительные методы
    def _executor(self, func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.semaphore.acquire()
            func(*args, **kwargs)
            self.semaphore.release()

        return wrapper
