def spell(*words):
    words = [word.lower() for word in words]
    result = {word[0]: 0 for word in words}

    for word in words:
        if len(word) > result.get(word[0]):
            result[word[0]] = len(word)

    return result


# def spell(*args):
#     result = {}
#     for word in args:
#         if result.get(word[0].lower(), 0) < len(word):
#             result[word[0].lower()] = len(word)
#     return result
