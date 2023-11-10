def sourcetemplate(url: str) -> callable:
    def queries_constructor(**kwargs) -> str:
        nonlocal url
        query_index = 0

        if len(kwargs) < 1:
            return url

        for key, value in sorted(kwargs.items()):
            if query_index == 0:
               url = url + f'?{key}={value}'
            else:
                url = url + f'&{key}={value}'
            query_index += 1

        return url
    return queries_constructor
