class IPAddress:
    def __init__(self, ipaddress: str | tuple):
        self.ipaddress = ipaddress

    @property
    def ipaddress(self):
        return self._ipaddress

    @ipaddress.setter
    def ipaddress(self, data: str | tuple | list):
        self._ipaddress = data if isinstance(data, str) else '.'.join(map(str, data))

    def __str__(self):
        return self._ipaddress

    def __repr__(self):
        return f"{type(self).__name__}('{self._ipaddress}')"
