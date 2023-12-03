import re

word, text = input(), input()
print(len(re.findall(rf'\b{word[:-3]}(our|or)?\b', text, re.I)))
