import concurrent.futures
import requests


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]


def get_request_header(url: str):
    return requests.get(url).headers


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(get_request_header, (link for link in sources))
    headers_stor = {source: next(results) for source in sources}
