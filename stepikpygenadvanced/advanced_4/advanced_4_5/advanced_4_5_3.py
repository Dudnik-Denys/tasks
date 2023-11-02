rows, columns = int(input()), int(input())
matrix = [list(map(int, input().split())) for row in range(rows)]
change = list(map(int, input().split()))


for row in range(rows):
    first = matrix[row][change[0]]
    second = matrix[row][change[1]]
    matrix[row][change[0]] = second
    matrix[row][change[1]] = first
    print(*matrix[row])
