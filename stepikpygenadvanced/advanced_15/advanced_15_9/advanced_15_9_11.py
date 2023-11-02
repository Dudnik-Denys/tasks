print(all(map(lambda x: x.isdigit() and 255 >= int(x) >= 0, input().split('.'))))
