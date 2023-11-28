import sys
import re

data = [line.strip() for line in sys.stdin]

for text in data:
    result = re.search(r'\b(\w+)\1\b', text)
    if result:
        print(result.group())
