data = input().split()
n = int(input())
result = []
size = int((len(data) / n) + 1)

for i in range(n):
    lst = []
    indx = i
    for j in range(size):
        if indx >= len(data):
            continue
        lst.append(data[indx])
        indx += n
    result.append(lst)

print(result)


# Крутое решение:

# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)
