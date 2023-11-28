import sys
import re

data = [number.strip() for number in sys.stdin]

for number in data:
    r = re.search(r'(?P<country>\d{1,3})([\s-])?(?P<city>\d{1,3})\2(?P<num>\d{4,10})', number)
    print(f'Код страны: {r.groupdict()["country"]}, Код города: {r.groupdict()["city"]}, Номер: {r.groupdict()["num"]}')
