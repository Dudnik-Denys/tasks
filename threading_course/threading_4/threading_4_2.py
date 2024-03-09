import threading
from typing import Callable


class MyThread(threading.Thread):
    def __init__(self, msg_error: str = "error", task: Callable = None):
        super().__init__()
        self.msg_error = msg_error
        self.task = task

    def run(self) -> None:
        try:
            if self.task is not None:
                self.task()
        except Exception as err:
            print(self.msg_error)
        finally:
            del self.task, self.msg_error
