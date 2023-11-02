with open('funcs.txt', mode='r', encoding='utf-8') as file:
    text = [line.strip() for line in file.readlines() if 'def' in line or '#' in line]

    for i in range(len(text)):
        if 'def' in text[i]:
            start = 'f'
            end = '('
            text[i] = text[i][text[i].index(start) + 1: text[i].index(end)].strip()

    normal = []
    problem = []

    for x in range(1, len(text)):
        if '#' not in text[x] and '#' in text[x - 1]:
            normal.append(text[x])

    for row in text:
        if '#' not in row and row not in normal:
            problem.append(row)

    if len(problem) >= 1:
        [print(i) for i in problem]
    else:
        print('Best Programming Team')
