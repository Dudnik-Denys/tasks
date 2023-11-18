def subdomain_visits(cpdomains: list[str]) -> list[str]:
    domains = dict()

    for elem in cpdomains:
        data = elem.split(' ')
        cnt = int(data[0])
        domain = data[1].split('.')
        for dom in range(len(domain)):
            k = '.'.join(domain[dom:])
            if k in domains:
                domains[k] += cnt
            else:
                domains = domains | {k: cnt}

    return [f'{v} {k}' for k, v in domains.items()]
