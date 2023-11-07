def without_cycles(n):
    print(n)
    if n > 0:
        without_cycles(n - 5)
        print(n)


without_cycles(16)
