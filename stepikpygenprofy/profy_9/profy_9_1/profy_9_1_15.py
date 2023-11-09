def zip_longest(*args, fill=None) -> list[tuple]:
    for elem in args:
        if not isinstance(elem, (list, tuple)):
            raise TypeError('Invalid input data, not all elements is sequence')

    result = []
    biggest_seq = max(args, key=len)

    for i in range(len(biggest_seq)):
        temp = []
        for seq in args:
            try:
                temp.append(seq[i])
            except IndexError:
                temp.append(fill)
        result.append(tuple(temp))

    return result
