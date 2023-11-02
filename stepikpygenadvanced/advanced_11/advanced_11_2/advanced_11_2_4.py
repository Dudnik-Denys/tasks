data = {'name': 'timur', 'age': 28}


def build_query_string(params: dict) -> str:
    srt = sorted(params)
    text = ''

    for i in range(len(srt)):
        if i < len(srt) - 1:
            text = text + srt[i] + '=' + str(params[srt[i]]) + '&'
        else:
            text = text + srt[i] + '=' + str(params[srt[i]])

    return text


# def build_query_string(params):
#     res = [f'{k}={v}' for k, v in params.items()]
#     return '&'.join(sorted(res))
