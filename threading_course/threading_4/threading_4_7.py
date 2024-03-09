import threading


class NoTargetException(Exception):
    pass


# Создаем класс потока
class MyThread(threading.Thread):
    def __init__(self, target=None, result=None):
        super().__init__()
        self.target = target
        self.result = result

    def run(self) -> None:
        if self.target is None:
            raise NoTargetException(threading.current_thread().name)
        self.result = self.target()


# Определяем функцию перехвата исключения
def custom_hook(exc):
    print(f'{threading.current_thread().name} (id={threading.current_thread().native_id}) failed')


# Назначаем ее перехватчиком )
threading.excepthook = custom_hook
