rows, columns = map(int, input().split())
matrix = [[0 for column in range(columns)] for row in range(rows)]


def diagonals(lines: int, cols: int, data: list):
    indx = 1

    for x in range(lines + cols):
        for y in range(lines):
            for z in range(cols):
                if z == x - y - 1:
                    data[y][z] = indx
                    indx += 1

    for i in data:
        print(*i)


diagonals(rows, columns, matrix)
