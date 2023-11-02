n = int(input())
data = [[0 for _ in range(n)] for _ in range(n)]


def diagonals(size: int, matrix: list):

    for i in range(size):
        for j in range(size):
            matrix[i][j] = abs(i - j)

    return matrix


for line in diagonals(n, data):
    print(*line)
