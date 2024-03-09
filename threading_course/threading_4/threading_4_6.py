import threading
import time
import random

start_time = time.monotonic()


def get_request_header(url):
    t = random.choice([0.3, 0.5, 0.7, 1, 1.5, 2])
    print(f'Process {threading.current_thread()} start slleping {t} seconds')
    time.sleep(t)
    return f'{url}_header'


class GetHeaders(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.url_headers = None

    def run(self):
        self.url_headers = {self.url: get_request_header(self.url)}


sources = ['url.ua', 'url.en', 'url.it', 'url.de', 'url.ro', 'url.fr', 'url.es', 'url.bg', 'url.at', 'url.be', 'url.br',
           'url.kz', 'url.pl', 'url.pt', 'url.sk']

threads = [GetHeaders(source) for source in sources]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join(2)

results = {}

for thread in threads:
    results.update(thread.url_headers)

print('Time of executing:', time.monotonic() - start_time)
