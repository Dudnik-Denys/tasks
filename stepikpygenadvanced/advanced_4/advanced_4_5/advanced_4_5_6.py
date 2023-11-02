n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
size = int(n / 2)

for i in range(size):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
