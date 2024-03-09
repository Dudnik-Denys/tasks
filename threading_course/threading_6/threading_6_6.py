from queue import Empty
from threading import Thread, current_thread
from datetime import datetime


# перепишите целевую функцию предыдущего задания с учетом нового условия работы
def task(t_wait: float):
    while True:
        try:
            elem = main_queue.get(timeout=t_wait)
            print(elem.id)
        except Empty:
            print(f'Empty {datetime.now()} thread = {current_thread().name}')
            break


# создайте и запустите один поток - инспектор с этой функцией
insp_1 = Thread(target=task, args=(t_wait,), name='insp_1', daemon=True)
insp_1.start()
insp_1.join()
