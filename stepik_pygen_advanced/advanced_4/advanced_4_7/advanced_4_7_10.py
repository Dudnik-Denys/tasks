rows_1, columns_1 = map(int, input().split())
data_1 = [list(map(int, input().split())) for _ in range(rows_1)]
empty = input()
rows_2, columns_2 = map(int, input().split())
data_2 = [list(map(int, input().split())) for _ in range(rows_2)]
[print(line) for line in data_1]
print()
[print(line) for line in data_2]


def matrix_multiply(matrix_1: list, matrix_2: list) -> list:
    result = []

    for i in range(rows_1):
        lst = []
        for j in range(columns_2):
            inner = []
            for k in range(rows_2):
                num = matrix_1[i][k] * matrix_2[k][j]
                inner.append(num)
            lst.append(sum(inner))
        result.append(lst)

    return result


for line in matrix_multiply(data_1, data_2):
    print(*line)
