from collections import ChainMap

def get_all_values(chainmap, key):
    return {d[key] for d in chainmap.maps if key in d}
