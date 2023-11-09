def hash_as_key(objects: list) -> dict:
    result = {}

    for obj in objects:
        if hash(obj) not in result:
            result[hash(obj)] = obj
        else:
            if isinstance(result[hash(obj)], list):
                result[hash(obj)].append(obj)
            else:
                result[hash(obj)] = [result[hash(obj)], obj]
    return result
