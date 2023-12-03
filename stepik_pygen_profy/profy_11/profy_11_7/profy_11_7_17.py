import re
import sys

d = {}
for line in sys.stdin:
    for i in re.finditer(r'<(\w+)>', line):
        d.setdefault(i.group(1), [])
    for i in re.finditer(r'<(\w+) .+?>', line):
        key = i.group(1)
        d.setdefault(key, []).extend(re.findall(r'\b([a-z-]+)=', i.group(0)))

for k, v in sorted(d.items()):
    print(f'{k}: {", ".join(sorted(set(v)))}')
