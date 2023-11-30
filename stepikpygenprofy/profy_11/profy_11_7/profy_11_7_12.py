import re

text, word = input(), input()
print(len(re.findall(r'\b' + word + r'\b', text)))
