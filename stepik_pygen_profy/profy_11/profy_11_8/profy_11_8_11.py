import re
import keyword

data = input()
lower_kw = [kw.lower() for kw in keyword.kwlist]


def replace_keyword(word: re.Match) -> str:
    return '<kw>' if word.group(0).lower() in lower_kw else word.group(0)


print(re.sub(r'\b\w+\b', replace_keyword, data))


# Пример более простого решения:
# import re
# import keyword
#
# keys = '|'.join(keyword.kwlist)
#
# print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))
