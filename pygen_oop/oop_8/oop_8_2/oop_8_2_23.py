from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        codes = {
            'информация': range(100, 200),
            'успех': range(200, 300),
            'перенаправление': range(300, 400),
            'ошибка клиента': range(400, 500),
            'ошибка сервера': range(500, 600)
        }
        for name, interval in codes.items():
            if self.value in interval:
                return name
