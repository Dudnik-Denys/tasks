import re
import sys

data = [line.strip() for line in sys.stdin]

for text in data:
    print(re.search(r'^_\d+[A-Za-z]*_?$', text) is not None)
