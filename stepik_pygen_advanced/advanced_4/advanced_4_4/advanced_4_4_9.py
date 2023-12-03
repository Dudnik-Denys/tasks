rows, columns = int(input()), int(input())
matrix = [[input() for column in range(columns)] for row in range(rows)]

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()

print()

for i in range(columns):
    for j in range(rows):
        print(matrix[j][i], end=' ')
    print()
