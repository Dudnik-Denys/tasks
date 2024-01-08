class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *slaves):
        for slave in slaves:
            self.juniors.append((slave, 'junior'))

    def add_senior(self, *seniors):
        for senior in seniors:
            self.seniors.append((senior, 'senior'))

    def __iter__(self):
        yield from self.juniors + self.seniors
