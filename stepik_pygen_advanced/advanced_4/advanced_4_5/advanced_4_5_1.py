rows, columns = int(input()), int(input())
matrix = [[0] * columns for column in range(rows)]

for row in range(rows):
    for column in range(columns):
        matrix[row][column] = row * column

[print(*row) for row in matrix]
