size = int(input())
words = [input().lower() for _ in range(size)]

for word in words:
    print(len(set(word)))
