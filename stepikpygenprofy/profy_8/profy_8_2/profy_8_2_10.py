def triangle(h):
    if h > 0:
        triangle(h - 1)
        print('*' * h)


triangle(3)
