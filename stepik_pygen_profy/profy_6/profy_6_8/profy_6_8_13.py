from collections import Counter

counter = Counter(input().lower().split())

print(*sorted([item for item in counter if counter[item] == counter[counter.most_common()[-1][0]]]), sep=', ')
