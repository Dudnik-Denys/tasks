from string import ascii_lowercase, ascii_uppercase


class CaesarCipher:
    def __init__(self, step):
        self.step = step

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, num):
        if num in range(1, 27):
            self._step = num

    def decode(self, text):
        pass
        result = ''
        for char in text:
            if char.islower() and char in ascii_lowercase:
                if ascii_lowercase.index(char) - self.step < 0:
                    result += ascii_lowercase[26 - (abs(ascii_lowercase.index(char) - self.step) % 26)]
                else:
                    result += ascii_lowercase[ascii_lowercase.index(char) - self.step]
            elif char.isupper() and char in ascii_uppercase:
                if ascii_uppercase.index(char) - self.step < 0:
                    result += ascii_uppercase[26 - (abs(ascii_uppercase.index(char) - self.step) % 26)]
                else:
                    result += ascii_uppercase[ascii_uppercase.index(char) - self.step]
            else:
                result += char
        return result

    def encode(self, text):
        result = ''
        for char in text:
            if char.islower() and char in ascii_lowercase:
                result += ascii_lowercase[(ascii_lowercase.index(char) + self.step) % 26]
            elif char.isupper() and char in ascii_uppercase:
                result += ascii_uppercase[(ascii_uppercase.index(char) + self.step) % 26]
            else:
                result += char
        return result


# Best solution
# from string import ascii_lowercase as low, ascii_uppercase as up
#
#
# class CaesarCipher:
#     def __init__(self, key):
#         self._encode = str.maketrans(low, low[key:] + low[:key]) | str.maketrans(up, up[key:] + up[:key])
#         self._decode = {v: k for k, v in self._encode.items()}
#
#     def encode(self, string):
#         return str.translate(string, self._encode)
#
#     def decode(self, string):
#         return str.translate(string, self._decode)
