n = int(input())
total = 0

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(matrix)):
    total += matrix[i][i]

print(total)
