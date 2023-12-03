n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
        if j == n - i - 1:
            matrix[i][j] = 1
    print(*matrix[i])
