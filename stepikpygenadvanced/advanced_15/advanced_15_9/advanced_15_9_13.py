from string import ascii_uppercase
from string import ascii_lowercase

data = input()

check_upper, check_lower, check_digit = 0, 0, 0

for char in data:
    if char in ascii_uppercase:
        check_upper += 1
    elif char in ascii_lowercase:
        check_lower += 1
    elif char.isdigit():
        check_digit += 1

print(['NO', 'YES'][check_upper > 0 and check_lower > 0 and check_digit > 0 and len(data) >= 7])


# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')
