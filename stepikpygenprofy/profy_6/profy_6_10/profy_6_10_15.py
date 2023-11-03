from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left=True):
    chainmap.maps = [chainmap.maps[::-1], chainmap.maps[:]][from_left]
    return chainmap.get(key)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'nam'))
