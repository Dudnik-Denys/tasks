n = int(input())
dct = {}

for i in range(n):
    data = input().split()
    data[2] = int(data[2])
    if data[0] not in dct:
        dct[data[0]] = {data[1]: data[2]}
    elif data[0] in dct and data[1] not in dct[data[0]]:
        dct[data[0]] |= {data[1]: data[2]}
    elif data[0] in dct and data[1] in dct[data[0]]:
        dct[data[0]][data[1]] += data[2]

names = sorted(dct)

for name in names:
    print(name + ':')
    values = sorted([val for val in dct[name]])
    for val in values:
        print(val, dct[name][val])

# data = {}
#
# for _ in range(int(input())):
#     name, product, count = input().split()
#     data.setdefault(name, {})
#     data[name][product] = data[name].get(product, 0) + int(count)
#
# for person, products in sorted(data.items()):
#     print(f'{person}:')
#     for product, count in sorted(products.items()):
#         print(product, count)
