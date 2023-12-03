import sys
import re

bee = 0
geek = 0

data = [line.strip() for line in sys.stdin]

for text in data:
    bee_check = re.search(r'(bee)[\w\s\d]*(bee)', text)
    geek_check = re.search(r'\bgeek\b', text)
    bee += 1 if bee_check else 0
    geek += 1 if geek_check else 0

print(bee, geek, sep='\n')
