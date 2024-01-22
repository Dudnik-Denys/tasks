class AppStore:
    def __init__(self):
        self.apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.remove(app)

    @staticmethod
    def block_application(app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)
