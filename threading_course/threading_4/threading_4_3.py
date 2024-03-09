import threading


# Создайте класс SimpleThread
class SimpleThread(threading.Thread):
    def __init__(self, function, data):
        super().__init__()
        self.function = function
        self.data = data

    def run(self) -> None:
        try:
            if self.function is not None:
                print(self.function(self.data))
        finally:
            del self.function, self.data
