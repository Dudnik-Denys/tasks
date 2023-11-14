def get_min_max(data: list) -> tuple | None:
    if not data:
        return None
    return data.index(min(data)), data.index(max(data))
