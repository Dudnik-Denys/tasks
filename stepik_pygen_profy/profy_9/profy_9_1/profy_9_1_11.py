def custom_isinstance(objects: list, typeinfo: type | tuple[type]) -> int:
    return sum([1 for obj in objects if isinstance(obj, typeinfo)])
