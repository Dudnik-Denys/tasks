class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if type(app) not in [type(x) for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory):
        self.name = "YouTube"
        self.memory_max = memory


class AppPhone:
    def __init__(self, contacts):
        self.name = "Phone"
        self.contacts = contacts
