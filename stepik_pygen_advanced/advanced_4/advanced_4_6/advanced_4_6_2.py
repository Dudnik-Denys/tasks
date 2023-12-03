n = int(input())
matrix = [[0] * n for _ in range(n)]


def secondary_diagonal(num: int, data: list):
    for i in range(num):
        for j in range(num):
            if j == num - i - 1:
                data[i][j] = 1
            if j > num - i - 1:
                data[i][j] = 2
        print(*data[i])


secondary_diagonal(n, matrix)
