rows, columns = map(int, input().split())
matrix = [[0 for _ in range(columns)] for _ in range(rows)]
indx = 0


def spiral(lines: int, cols: int, data: list):
    num = 1
    direction = "right"
    x = 0  # horizontal
    y = 0  # vertical
    line_size = lines
    column_size = cols

    if line_size <= column_size:
        while lines != 0:
            if direction == "right":
                for i in range(cols):
                    data[x][y] = num
                    num += 1
                    y += 1
                lines -= 1
                y -= 1
                x += 1
                direction = "down"
            elif direction == "down":
                for i in range(lines):
                    data[x][y] = num
                    num += 1
                    x += 1
                cols -= 1
                x -= 1
                y -= 1
                direction = "left"
            elif direction == "left":
                for i in range(cols):
                    data[x][y] = num
                    num += 1
                    y -= 1
                y += 1
                lines -= 1
                x -= 1
                direction = "up"
            elif direction == "up":
                for i in range(lines):
                    data[x][y] = num
                    num += 1
                    x -= 1
                cols -= 1
                x += 1
                y += 1
                direction = "right"

    if line_size > column_size:
        while cols != 0:
            if direction == "right":
                for i in range(cols):
                    data[x][y] = num
                    num += 1
                    y += 1
                lines -= 1
                y -= 1
                x += 1
                direction = "down"
            elif direction == "down":
                for i in range(lines):
                    data[x][y] = num
                    num += 1
                    x += 1
                cols -= 1
                x -= 1
                y -= 1
                direction = "left"
            elif direction == "left":
                for i in range(cols):
                    data[x][y] = num
                    num += 1
                    y -= 1
                y += 1
                lines -= 1
                x -= 1
                direction = "up"
            elif direction == "up":
                for i in range(lines):
                    data[x][y] = num
                    num += 1
                    x -= 1
                cols -= 1
                x += 1
                y += 1
                direction = "right"

    for i in range(line_size):
        print(*data[i])


spiral(rows, columns, matrix)
