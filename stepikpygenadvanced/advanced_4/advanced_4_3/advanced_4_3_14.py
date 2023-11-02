data = input().split()


def under_list(lst: list) -> list:
    res = [[]]
    index = 0
    if len(lst) == 0:
        return res
    for i in range(1, len(data) + 1):
        for j in range(len(data) - index):
            res.append(data[j:j + i])
        index += 1
    return res


print(under_list(data))
