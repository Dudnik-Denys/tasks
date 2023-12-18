class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(hexcode[0:2], 16)
        self.g = int(hexcode[2:4], 16)
        self.b = int(hexcode[4:6], 16)
