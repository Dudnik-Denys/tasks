import re

regex_obj = re.compile(r'\d+')
start, finish = map(int, input().split())
digits = regex_obj.findall(input(), pos=start, endpos=finish)
print(sum([int(digit) for digit in digits]))
