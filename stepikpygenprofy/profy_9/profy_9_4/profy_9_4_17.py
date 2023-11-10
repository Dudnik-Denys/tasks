def polynom(num: int) -> int:
    result = (num ** 2) + 1
    if 'values' not in polynom.__dict__:
        polynom.values = {result}
    else:
        polynom.values.add(result)
    return result
