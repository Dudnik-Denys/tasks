import threading
import time


def test(timeout: int) -> None:
    print(f"{threading.current_thread().name} started")
    time.sleep(timeout)
    print(f"{threading.current_thread().name} executed")


print('MainThread START --->')
timer = threading.Timer(interval=1, function=test, args=(3, ))
timer.name = "my_timer"
timer.start()
timer.join(1)
timer.cancel()
print('---> MainThread FINISH')
