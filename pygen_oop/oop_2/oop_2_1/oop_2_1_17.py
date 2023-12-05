def pluck(data: dict, path: str, default=None):
    if '.' not in path:
        return data.get(path, default)

    path = path.split('.')

    for key in path:
        data = data.get(key, default)
    return data
