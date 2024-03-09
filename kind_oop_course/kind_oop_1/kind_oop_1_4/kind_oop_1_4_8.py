import sys


class StreamData:
    def create(self, fields: tuple[str], lst_values: list[str]):
        if len(fields) == len(lst_values):
            self.__dict__.update({key: value for key, value in dict(zip(fields, lst_values)).items()})
            return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()