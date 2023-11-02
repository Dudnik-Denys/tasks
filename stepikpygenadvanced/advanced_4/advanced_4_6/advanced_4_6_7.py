rows, columns = map(int, input().split())
matrix = [[0 for column in range(columns)] for row in range(rows)]


def diagonals(lines: int, cols: int, data: list):
    indx = 0
    for i in range(lines):
        if indx == cols:
            indx = 0
        inner_index = indx + 1
        lower_index = 1
        for j in range(cols):
            if inner_index <= cols:
                data[i][j] = inner_index
                inner_index += 1
            elif inner_index > cols:
                data[i][j] = lower_index
                lower_index += 1
        indx += 1
        print(*data[i])


diagonals(rows, columns, matrix)

# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()
