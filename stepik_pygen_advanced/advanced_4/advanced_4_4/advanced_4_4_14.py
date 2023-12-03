n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
total_u, total_r, total_d, total_l = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if j > i and i < n - 1 - j:
            total_u += matrix[i][j]
        elif j > i and i > n - 1 - j:
            total_r += matrix[i][j]
        elif i > j and i > n - 1 - j:
            total_d += matrix[i][j]
        elif i > j and i < n - 1 - j:
            total_l += matrix[i][j]

print(f'Верхняя четверть: {total_u}\n'
      f'Правая четверть: {total_r}\n'
      f'Нижняя четверть: {total_d}\n'
      f'Левая четверть: {total_l}')
