import threading

# Произвольная функция
get_request_header = lambda url: {'header': 'header'}


# Допишите код здесь
class GetHeaders(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.url_headers = None

    def run(self):
        self.url_headers = {self.url: get_request_header(self.url)}
