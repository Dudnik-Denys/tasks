import sys
import re

data = [line.strip() for line in sys.stdin]

score = 0

for text in data:
    if re.search(r'^(beegeek).*(beegeek)$', text):
        score += 3
    elif re.search(r'^(beegeek)|(beegeek)$', text):
        score += 2
    elif re.search(r'.*(beegeek).*', text):
        score += 1

print(score)
