text = input().split()
dct = {}

for word in text:
    dct[word] = dct.get(word, 0) + 1
    print(dct[word], end=' ')
