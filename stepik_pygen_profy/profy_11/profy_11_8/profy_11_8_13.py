import re


def func_multi(match_obj):
    multiplicator, text = match_obj.groups()
    res = int(multiplicator) * text
    return res


def func_rec(string):
    new = re.sub(r'(\d+)\((\w+)\)', func_multi, string)
    if new == string:
        return new
    return func_rec(new)


data = input()
print(func_rec(data))

# Можно упростить до:
# import re
#
# s = input()
# while '(' in s:
#     s = re.sub(r'(\d+)\((\w+)\)', lambda x: x[2] * int(x[1]), s)
# print(s)
