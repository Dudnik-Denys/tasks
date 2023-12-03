n = int(input())
matrix = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = '*'
        if j == n - 1 - i:
            matrix[i][j] = '*'
        if (n / 2) > j > (n / 2) - 1:
            matrix[i][j] = '*'
        if (n / 2) > i > (n / 2) - 1:
            matrix[i][j] = '*'

for line in matrix:
    print(*line)
