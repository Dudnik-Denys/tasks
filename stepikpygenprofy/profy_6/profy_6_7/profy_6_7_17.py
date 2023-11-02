from collections import Counter

[print(f'{key}: {value}') for key, value in sorted(Counter(input().split(',')).items())]
