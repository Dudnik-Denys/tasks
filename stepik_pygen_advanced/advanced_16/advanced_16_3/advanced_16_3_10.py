s = [input() for _ in range(int(input()))]


def gem(x):
    return sum([ord(i.upper()) - 65 for i in x])


[print(i) for i in sorted(s, key=lambda x: (gem(x), x))]
