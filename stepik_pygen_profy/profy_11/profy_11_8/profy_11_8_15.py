import re
import sys

regex = r'\n#.*?$|' \
        r'\s*""".*?"""|' \
        r'\n? *#.*?$'

s = sys.stdin.read()
print(re.sub(regex, '', s, flags=re.S | re.M))
