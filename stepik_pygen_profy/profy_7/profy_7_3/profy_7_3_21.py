def add_to_list_in_dict(data: dict, key, element):
    try:
        data[key].append(element)
    except TypeError:
        pass
    except KeyError:
        data[key] = [element]
