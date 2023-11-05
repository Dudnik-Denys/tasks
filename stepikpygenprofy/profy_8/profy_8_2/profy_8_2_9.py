def triangle(h: int):
    if h > 0:
        print('*' * h)
        triangle(h - 1)


triangle(3)