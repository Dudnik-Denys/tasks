import re
import sys

data = [line.strip() for line in sys.stdin]
print(sum([1 for text in data if re.search(r'beegeek', text, re.I)]))
