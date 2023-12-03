m, n = int(input()), int(input())
books_1 = [input() for _ in range(m)]
books_2 = [input() for _ in range(n)]

for book in books_2:
    if book in books_1:
        print('YES')
    else:
        print('NO')
