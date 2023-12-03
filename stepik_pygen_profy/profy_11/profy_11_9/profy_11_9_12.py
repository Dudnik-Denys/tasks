import re


def multiple_split(string, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, string)
