import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        data = [elem.split(' ') for elem in data]
        for elem in data:
            self.lst_data.append({key: value for key, value in dict(zip(self.FIELDS, elem)).items()})

    def select(self, a, b):
        if a > len(self.lst_data):
            return []
        if b >= len(self.lst_data):
            return self.lst_data
        return self.lst_data[a:b + 1]

db = DataBase()
db.insert(lst_in)
