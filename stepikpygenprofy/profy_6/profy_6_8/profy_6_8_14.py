from collections import Counter

print(sorted(Counter(input().lower().split()).items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0])
