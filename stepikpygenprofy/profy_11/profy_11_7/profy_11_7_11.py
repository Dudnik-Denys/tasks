import re

text, word = input(), input()
print(len(re.findall(f'\B{word}\B', text)))
