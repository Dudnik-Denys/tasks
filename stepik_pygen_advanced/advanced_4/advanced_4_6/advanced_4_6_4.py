rows, columns = map(int, input().split())
matrix = [[0 for column in range(columns)] for row in range(rows)]
indx = 0

for row in range(rows):
    indx += 1
    inner_index = indx
    for column in range(columns):
        matrix[row][column] = inner_index
        inner_index += rows
    print(*matrix[row])
