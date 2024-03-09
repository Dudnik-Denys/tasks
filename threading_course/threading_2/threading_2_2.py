import threading
from time import sleep

# Функция может быть реализована по-разному, в зависимости от теста
test = lambda: sleep(3)

tr = threading.Thread(target=test, daemon=True)
tr.start()
tr.join(timeout=2)
