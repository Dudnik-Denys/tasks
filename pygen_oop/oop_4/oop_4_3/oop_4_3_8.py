class Gun:
    def __init__(self):
        self.shots = 0

    def shoot(self):
        print(['pif', 'paf'][self.shots % 2])
        self.shots += 1

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.shots = 0
