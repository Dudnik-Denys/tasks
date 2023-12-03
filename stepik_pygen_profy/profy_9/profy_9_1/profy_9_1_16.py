text = [symbol for symbol in input()]
print(''.join(sorted(text, key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit() and int(x) % 2 != 0, x.isupper(), x, x.islower()))))
