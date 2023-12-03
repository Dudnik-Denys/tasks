rows, columns = map(int, input().split())
data_1 = [list(map(int, input().split())) for _ in range(rows)]
data_2 = [list(map(int, input().split())) for _ in range(rows)]


def matrix_add(matrix_1: list, matrix_2: list) -> list:
    result = []

    for i in range(rows):
        lst = []
        for j in range(columns):
            lst.append(matrix_1[i][j] + matrix_2[i][j])
        result.append(lst)

    return result


for line in matrix_add(data_1, data_2):
    print(*line)
