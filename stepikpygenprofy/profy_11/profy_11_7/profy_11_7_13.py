import re

word, text = input(), input()
print(len(re.findall(rf'\b{word[:-2]}(se|ze)\b', text, re.I)))
