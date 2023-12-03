rows, columns = int(input()), int(input())
matrix = [list(map(int, input().split())) for row in range(rows)]
max_value = -100
max_data = []

for row in range(rows):
    for column in range(columns):
        if matrix[row][column] > max_value:
            max_value = matrix[row][column]
            max_data.clear()
            max_data.append(row)
            max_data.append(column)

print(*max_data)
