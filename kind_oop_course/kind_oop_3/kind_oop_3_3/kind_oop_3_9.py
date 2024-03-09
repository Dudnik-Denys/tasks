class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __repr__(self):
        time = self.get_time() if self.get_time() > 0 else 0
        hours = time // 3600
        time -= (hours * 3600)
        minutes = time // 60
        time -= (minutes * 60)

        return f"{'0' + str(hours) if hours < 10 else hours}: {'0' + str(minutes) if minutes < 10 else minutes}: " \
               f"{'0' + str(time) if time < 10 else time}"

    def __len__(self):
        return self.get_time() if self.get_time() > 0 else 0

    def get_time(self):
        return self.clock1.get_time() - self.clock2.get_time()


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
