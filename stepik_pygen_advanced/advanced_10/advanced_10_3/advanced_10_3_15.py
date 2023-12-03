words = input().lower().split()
words = [word.strip('.,!?:;-') for word in words]
result = {}

for word in words:
    result[word] = result.get(word, 0) + 1

print(sorted(result.items(), key=lambda item: (item[1], item[0]))[0][0])
