def hash_function(obj):
    obj = str(obj)
    indx = 1
    temp1 = 0
    temp2 = ord(obj[0])

    for elem in range(len(obj) // 2):
        temp1 += (ord(obj[elem]) * ord(obj[elem - indx]))
        indx += 2
    temp1 += ord(obj[len(obj) // 2]) if len(obj) % 2 else 0

    for elem in range(1, len(obj)):
        if not elem % 2:
            temp2 += (ord(obj[elem]) * (elem + 1))
        else:
            temp2 -= (ord(obj[elem]) * (elem + 1))

    return (temp1 * temp2) % 123456791
