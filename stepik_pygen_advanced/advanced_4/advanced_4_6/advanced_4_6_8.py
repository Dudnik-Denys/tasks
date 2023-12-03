rows, columns = map(int, input().split())
matrix = [[0 for column in range(columns)] for row in range(rows)]


def snake(lines: int, cols: int, data: list):
    indx = 1

    for i in range(lines):
        for j in range(cols):
            if i % 2 == 0:
                data[i][j] = indx
            elif i % 2 != 0:
                data[i][cols - 1 - j] = indx
            indx += 1
        print(*data[i])


snake(rows, columns, matrix)
