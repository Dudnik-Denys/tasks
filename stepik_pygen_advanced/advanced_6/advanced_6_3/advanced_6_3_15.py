num = int(input())


def tribonacci(size: int):
    base_triboancci = (1, 1, 1)

    if size == 1:
        return base_triboancci[0],
    if size == 2:
        return base_triboancci[:2]
    if size == 3:
        return base_triboancci
    if size > 3:
        for i in range(size - 3):
            new_elem = sum(base_triboancci[i:i + 3]),
            base_triboancci = base_triboancci + new_elem
        return base_triboancci


for elem in tribonacci(num):
    print(elem, end=' ')
