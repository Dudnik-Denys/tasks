import threading
import time


def do_request(card_number: str) -> None:
    time.sleep(2)


valid_num = 4007000000028
cards = [str(valid_num + i) for i in range(72)]
start = time.monotonic()
threads = []

for card in cards:
    thread = threading.Thread(target=do_request, args=(card,), daemon=True)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join(4)
