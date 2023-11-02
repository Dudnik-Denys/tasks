size = int(input())
words = ''.join([input().lower() for _ in range(size)])
print(len(set(words)))
