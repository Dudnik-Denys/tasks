data = input().split()
result = {}
text = []

for elem in data:
    result[elem] = result.get(elem, 0) + 1

for elem in data:
    if elem in result and elem not in text:
        text.append(elem)
    elif elem in result and elem in text:
        text.append(elem + '_' + str(data.count(elem) - (result[elem] - 1)))
        result[elem] -= 1

print(*text)


# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1
