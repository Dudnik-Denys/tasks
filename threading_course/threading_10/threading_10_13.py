import concurrent.futures
from time import sleep

sources = ["url_1",
           "url_2",
           "url_3",
           "url_4",
           "url_5"]


def get_request_header(url: str) -> str:
    if url == "url_1":
        sleep(0.8)
    if url == "url_2":
        sleep(0.9)
    if url == "url_3":
        sleep(1.4)
    if url == "url_4":
        sleep(3)
    if url == "url_5":
        sleep(1.6)
    return f"{url}-headers"


headers_stor = {}
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
try:
    futures = {executor.submit(get_request_header, url): url for url in sources}
    done, not_done = concurrent.futures.wait(futures, timeout=1.45)
    for future in done:
        headers_stor[futures[future]] = future.result()
    for future in not_done:
        headers_stor[futures[future]] = "no_response"
finally:
    executor.shutdown(wait=False)
