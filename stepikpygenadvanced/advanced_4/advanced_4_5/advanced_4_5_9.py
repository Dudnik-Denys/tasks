n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def magic_square(num: int, data: list) -> str:
    summ = sum(data[0])
    main_diagonal = []
    secondary_diagonal = []
    all_lines = []

    for row in data:
        if 0 in row or len(set(row)) != len(row):
            return 'NO'
        for elem in row:
            all_lines.append(elem)

    if len(all_lines) != len(set(all_lines)):
        return 'NO'

    for i in range(num):
        if sum(data[i]) != summ:
            return 'NO'
        column = []
        for j in range(num):

            column.append(data[j][i])

            if i == j:
                main_diagonal.append(data[i][i])
            if j == num - i - 1:
                secondary_diagonal.append(data[i][num - i - 1])

        if sum(column) != summ:
            return 'NO'

    if sum(main_diagonal) != summ or sum(secondary_diagonal) != summ:
        return 'NO'

    return 'YES'


print(magic_square(n, matrix))
