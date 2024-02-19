from re import compile, fullmatch


class DomainException(Exception):
    pass


class Domain:
    _PATTERN = compile(r'[a-z]+\.[a-z]+')

    def __init__(self, domain):
        self.domain = domain

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        if fullmatch(self._PATTERN, value) is None:
            raise DomainException('Недопустимый домен, url или email')
        self._domain = value

    @staticmethod
    def from_url(url):
        if url.startswith('https://') or url.startswith('http://'):
            return Domain(url[7:] if url.startswith('http://') else url[8:])
        raise DomainException('Недопустимый домен, url или email')

    @staticmethod
    def from_email(email):
        if fullmatch(r'[a-z]+@.+', email) is not None:
            return Domain(email[email.index('@') + 1:])
        raise DomainException('Недопустимый домен, url или email')

    def __str__(self):
        return self.domain
