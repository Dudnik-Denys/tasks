rows, columns = map(int, input().split())
matrix = []

for row in range(rows):
    elem = []
    for column in range(columns):
        elem.append('*')
    matrix.append(elem)

for row in range(rows):
    for column in range(columns):
        if row % 2 == 0 and column % 2 == 0:
            matrix[row][column] = '.'
        if row % 2 != 0 and column % 2 != 0:
            matrix[row][column] = '.'

[print(*line) for line in matrix]
