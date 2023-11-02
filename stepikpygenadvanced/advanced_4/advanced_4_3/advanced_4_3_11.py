n = int(input())

k = [1]

for i in range(1, n + 1):
    if i == 1:
        print(*k)
    elif i > 1:
        m = [1]
        for j in range(len(k) - 1):
            new_elem = k[j] + k[j + 1]
            m.append(new_elem)
        m.append(1)
        k = m
        print(*k)
