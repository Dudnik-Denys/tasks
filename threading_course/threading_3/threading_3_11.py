from threading import Timer, Thread
from typing import Callable
from time import sleep

result = False
func_1,  func_2 = lambda *x: sleep(x[0]), lambda: print('Execute completed!')


def callback_handler(task: Callable = None, args=(), callback_task: Callable = None) -> None:
    # не меняйте значение result
    # дополните код
    global result
    result = True if args[0] <= 3 else result
    thread = Thread(target=task, args=args)
    thread.start()
    timer = Timer(interval=0.3 + 0.05, function=callback_task)
    timer.start()
    thread.join(0.3)
    if result is False:
        timer.cancel()
        timer.join()
    timer.join()


callback_handler(func_1, (2,), func_2)
