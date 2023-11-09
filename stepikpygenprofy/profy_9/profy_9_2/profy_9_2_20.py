data = eval(input())

if type(data) == list:
    print(data[-1])
elif type(data) == tuple:
    print(data[0])
else:
    print(len(data))
