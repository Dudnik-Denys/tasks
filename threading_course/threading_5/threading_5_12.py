from queue import Queue
from threading import Thread
import time

# Функции handler(), is_valid() и timeout_handler() заданы в тестирующей программе

# Динамические очереди (размер не задан)
valid_queue = Queue()
none_valid_queue = Queue()


def task():
    while True:
        # Если производитель не успевает заполнять очередь, потребитель ожидает когда слот заполнится
        elem = valid_queue.get()
        handler(elem)


def main():
    # Нужно взывать функцию и получить объект генератора
    for elem in get_obj():
        if is_valid(elem):
            valid_queue.put(elem)
        else:
            none_valid_queue.put(elem)

# Демонические потоки автоматически будут убиты в момент завершения главного потока
t1 = Thread(target=task, daemon=True)
t2 = Thread(target=task, daemon=True)

# После старта, ожидают добавления элементов в очередь, чтобы извлечь и обработать
t1.start()
t2.start()

# Возникла блокирующая операция, главный поток создает поток производителя
main_th = Thread(target=main)

# Начинает валидировать и добавлять элементы в очередь
main_th.start()

# Задача производителя приоритетнее задач потребителей. Надо дождаться полного ее завершения
main_th.join() # Пока ждем завершения, потребители продолжают работать

# Прежде чем убить демонические потоки, нужно подождать заданное время
time.sleep(timeout_handler)
