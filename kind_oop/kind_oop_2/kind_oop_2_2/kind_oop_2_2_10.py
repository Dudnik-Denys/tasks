class PathLines:
    def __init__(self, *lines):
        self.lines = [LineTo(0, 0)] + [line for line in lines]

    def get_path(self):
        return self.lines[1:]

    def get_length(self):
        result = 0

        if len(self.lines) >= 2:
            sequence = self.lines[::-1]

            for i in range(len(sequence[:-1])):
                temp = (((sequence[i].x - sequence[i + 1].x) ** 2) + (sequence[i].y - sequence[i + 1].y) ** 2) ** .5
                result += temp

        return result

    def add_line(self, line):
        if isinstance(line, LineTo):
            self.lines.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
