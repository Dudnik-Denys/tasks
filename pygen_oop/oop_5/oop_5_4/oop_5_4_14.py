class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def copy(self, func=lambda x: x, transpose=False):
        if transpose:
            matrix = Matrix(self.cols, self.rows)
        else:
            matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                value = func(self.get_value(row, col))
                if transpose:
                    matrix.set_value(col, row, value)
                else:
                    matrix.set_value(row, col, value)
        return matrix

    def __str__(self):
        rows = (' '.join(map(str, row)) for row in self.matrix)
        return '\n'.join(rows)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return self.copy(func=lambda x: -x)

    def __invert__(self):
        return self.copy(transpose=True)

    def __round__(self, n=0):
        return self.copy(func=lambda x: round(x, n))
