import time
import threading

headers_stor_test = {}

sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]


def get_request_header(url: str):
    time.sleep(0.8)
    headers_stor_test[url] = "OK"


start_time = time.perf_counter()  # запускаем отсчет времени проверки решения

threads = []

for source in sources:
    thread = threading.Thread(target=get_request_header, args=(source,))
    thread.start()
    threads.append(thread)

for tr in threads:
    tr.join()

try:
    delta_time = time.perf_counter() - start_time
    assert delta_time <= 1
except AssertionError:
    raise Exception("!!! решение не приводит к быстродействию !!!")
print(*headers_stor_test.values(), sep="")
