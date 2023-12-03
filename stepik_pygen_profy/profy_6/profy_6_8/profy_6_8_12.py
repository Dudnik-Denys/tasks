from collections import Counter

counter = Counter(input().lower().split())
print(counter.most_common()[0][0])
