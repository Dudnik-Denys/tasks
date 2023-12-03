n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]


def latin_square(size: int, matrix: list):
    errors = 0

    for i in range(size):
        if errors > 0:
            break
        for j in range(2):
            nums = [num for num in range(1, n + 1)]
            for k in range(size):
                if j == 0:
                    if matrix[i][k] in nums:
                        nums.remove(matrix[i][k])
                    else:
                        errors += 1
                if j == 1:
                    if matrix[k][i] in nums:
                        nums.remove(matrix[k][i])
                    else:
                        errors += 1

    return ['YES', 'NO'][errors > 0]


print(latin_square(n, data))

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)
