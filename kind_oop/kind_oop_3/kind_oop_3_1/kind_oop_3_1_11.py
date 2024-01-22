import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, fl):
        if slot_num == 1 and isinstance(fl, Mechanical):
            self.slot_1 = fl
        if slot_num == 2 and isinstance(fl, Aragon):
            self.slot_2 = fl
        if slot_num == 3 and isinstance(fl, Calcium):
            self.slot_3 = fl

    def remove_filter(self, slot_num):
        self.__dict__[f'slot_{slot_num}'] = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        if self.slot_1 is not None and self.slot_2 is not None and self.slot_3 is not None:
            for num in range(1, 4):
                if not (0 <= (time.time() - self.__dict__[f'slot_{num}'].date) <= self.MAX_DATE_FILTER):
                    return False
            return True
        return False


class CheckSlot:
    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        if self._name not in instance.__dict__:
            instance.__dict__[self._name] = value


class Mechanical:
    date = CheckSlot()

    def __init__(self, date):
        self.date = date


class Aragon:
    date = CheckSlot()

    def __init__(self, date):
        self.date = date


class Calcium:
    date = CheckSlot()

    def __init__(self, date):
        self.date = date
