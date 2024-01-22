class Clock:
    def __init__(self, time=0):
        self.__time = time

    def get_time(self):
        return self.__time

    def set_time(self, tm):
        self.__time = tm if self.check_time(tm) else self.__time

    @staticmethod
    def check_time(tm):
        return 0 <= tm < 100_000 if type(tm) == int else False
