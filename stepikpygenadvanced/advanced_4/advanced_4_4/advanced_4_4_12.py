n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
maximum = matrix[0][0]  # бесполезный
new = []

for i in range(n):
    for j in range(n):
        if j > i:
            continue
        else:
            new.append(matrix[i][j])

print(max(new))
