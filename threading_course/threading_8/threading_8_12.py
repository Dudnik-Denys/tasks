def permission():
    # Ничего не печатает, возвращает только True | False
    # Обращаться можно только к атрибутам stor_local
    stor_local.counter = 0 if not hasattr(stor_local, 'counter') else stor_local.counter
    stor_local.counter += 1 if hasattr(stor_local, 'permission') else 0
    return stor_local.counter == 2
