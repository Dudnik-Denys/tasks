import re

print(*re.split(r'\s*(?:and|or|&|\|)\s*', input()), sep=', ')
