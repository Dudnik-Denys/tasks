matrix = ['. . . . . . . .'.split() for _ in range(8)]
data = input()
position = [ord(data[0]) - 97, abs(int(data[1]) - 8)]
matrix[position[1]][position[0]] = 'Q'

for i in range(8):
    for j in range(8):
        if abs(position[1] - i) * abs(position[0] - j) == 2:
            matrix[i][j] = '*'

[print(*line) for line in matrix]

# Пояснение: можно заметить, что для подходящих клеток выполняется равенство |x - x2| = 1 и |y - y2| = 2
# или |x - x2| = 2 и |y - y2| = 1. То есть либо разница по иксу равна единице и по игреку - двойке, либо, наоборот,
# разница по иксу равна двойке, а по игреку единице - единице. Это можно заменить равносильным условием произведение
# разниц равно двойке.
























# matrix = ['. . . . . . . .'.split() for _ in range(8)]
# data = input()
# position = [ord(data[0]) - 97, abs(int(data[1]) - 8)]
# matrix[position[1]][position[0]] = 'N'
#
# try:
#     if position[1] - 1 >= 0 and position[0] - 2 >= 0:
#         matrix[position[1] - 1][position[0] - 2] = '*'
#     if position[1] + 1 <= 7 and position[0] - 2 >= 0:
#         matrix[position[1] + 1][position[0] - 2] = '*'
#     if position[1] - 2 >= 0 and position[0] + 1 <= 7:
#         matrix[position[1] - 2][position[0] + 1] = '*'
#     if position[1] - 1 >= 0 and position[0] + 2 <= 7:
#         matrix[position[1] - 1][position[0] + 2] = '*'
#     if position[1] + 2 <= 7 and position[0] + 1 <= 7:
#         matrix[position[1] + 2][position[0] + 1] = '*'
#     if position[1] + 1 <= 7 and position[0] + 2 <= 7:
#         matrix[position[1] + 1][position[0] + 2] = '*'
#     if position[1] - 2 >= 0 and position[0] - 1 >= 0:
#         matrix[position[1] - 2][position[0] - 1] = '*'
#     if position[1] + 2 <= 7 and position[0] - 1 >= 0:
#         matrix[position[1] + 2][position[0] - 1] = '*'
# except IndexError:
#     pass
#
# [print(*line) for line in matrix]
