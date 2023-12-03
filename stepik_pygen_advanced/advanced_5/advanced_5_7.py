matrix = ['. . . . . . . .'.split() for _ in range(8)]
data = input()
position = [ord(data[0]) - 97, abs(int(data[1]) - 8)]

for i in range(8):
    for j in range(8):
        if i == position[1] or j == position[0] or abs(position[1] - i) ** 2 == abs(position[0] - j) ** 2:
            matrix[i][j] = '*'

matrix[position[1]][position[0]] = 'Q'
[print(*line) for line in matrix]
