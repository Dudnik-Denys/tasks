from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value):
    if type(key).__dict__['__hash__'] is None:
        return None
    if key not in chainmap:
        chainmap.maps[0].update({key: value})
        return None
    for i in range(len(chainmap.maps)):
        if key in chainmap.maps[i]:
            chainmap.maps[i][key] = value
    return chainmap
