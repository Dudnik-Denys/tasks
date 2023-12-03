from re import sub

pattern = r'(\b\w+\b)(\W+\1\b)+'

print(sub(pattern, r'\1', input()))
