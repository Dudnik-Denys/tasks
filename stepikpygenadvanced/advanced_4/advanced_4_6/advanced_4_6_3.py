rows, columns = map(int, input().split())
matrix = [[0 for column in range(columns)] for row in range(rows)]
indx = 0

for row in range(rows):
    for column in range(columns):
        indx += 1
        matrix[row][column] = indx
    print(*matrix[row])
