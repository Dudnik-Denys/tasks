def pretty_print(data: list, side='-', delimiter='|'):
    data = [str(num) for num in data]
    str_main = f'{delimiter} {(" " + delimiter + " ").join(data)} {delimiter}'
    print(f' {side*(len(str_main)-2)}')
    print(str_main)
    print(f' {side*(len(str_main)-2)}')
