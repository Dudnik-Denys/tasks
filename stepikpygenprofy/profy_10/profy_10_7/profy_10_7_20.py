def stop_on(iterable, obj):
    for elem in iterable:
        if elem != obj:
            yield elem
        else:
            return StopIteration
