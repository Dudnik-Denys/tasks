import copy

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
m = int(input())


def matrix_power(size: int, matrix: list, power: int) -> list:
    result = copy.deepcopy(matrix)

    for p in range(power - 1):
        for i in range(size):
            lst = []
            for j in range(size):
                inner = []
                for k in range(size):
                    num = result[i][k] * matrix[k][j]
                    inner.append(num)
                lst.append(sum(inner))
            result[i] = lst

    return result


for line in matrix_power(n, data, m):
    print(*line)
