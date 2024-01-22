class Server:
    __COUNTER = 0

    def __new__(cls, *args, **kwargs):
        cls.__COUNTER += 1
        new_server = object.__new__(cls)
        setattr(new_server, 'ip', cls.__COUNTER)
        return new_server

    def __init__(self):
        self.buffer = []
        self.linked_router = None

    def get_ip(self):
        return self.__dict__['ip']

    def get_data(self):
        copy = self.buffer[:]
        self.buffer.clear()
        return copy

    def send_data(self, data):
        if self.linked_router is not None:
            self.linked_router.buffer.append(data)


class Router:
    def __init__(self):
        self.buffer = []
        self.linked_servers = []

    def link(self, server):
        self.linked_servers.append(server)
        server.linked_router = self

    def unlink(self, server):
        self.linked_servers.remove(server)
        server.linked_router = None

    def send_data(self):
        copy = self.buffer[:]
        self.buffer.clear()
        for server in self.linked_servers:
            for msg in copy:
                if msg.ip == server.ip:
                    server.buffer.append(msg)


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
