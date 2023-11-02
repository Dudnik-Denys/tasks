n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
new = []

for i in range(n):
    l = []
    for j in range(n):
        l.append(matrix[j][i])
    l.reverse()
    new.append(l)

[print(row) for row in new]
