n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for line in matrix:
    line.reverse()

errors = 0

for i in range(n - 1):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            errors += 1
            break


print(['YES', 'NO'][errors > 0])


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# res = 'YES'
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if arr[i][j] != arr[n - j - 1][n - i - 1]:
#             res = 'NO'
#             break
#     if res == 'NO':
#         break
# print(res)
