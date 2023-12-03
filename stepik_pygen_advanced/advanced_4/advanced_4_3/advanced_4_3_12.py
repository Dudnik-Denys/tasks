string = input().split()
symbols = []

new = [string[0]]

for i in range(len(string) - 1):
    if i == len(string) - 2:
        if string[i] == string[i + 1]:
            new.append(string[i + 1])
            symbols.append(new)
        else:
            symbols.append(new)
            symbols.append([string[i + 1]])
    elif string[i] == string[i + 1]:
        new.append(string[i + 1])
    else:
        symbols.append(new)
        new = [string[i + 1]]

print(symbols)


# res = []
#
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
#
# print(res)
