rows, columns = int(input()), int(input())
matrix = [[input() for column in range(columns)] for row in range(rows)]

for lst in matrix:
    print(*lst)
