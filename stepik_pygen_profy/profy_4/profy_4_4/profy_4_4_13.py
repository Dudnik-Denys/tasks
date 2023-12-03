import json
from datetime import datetime

with open('pools.json', encoding='utf-8') as pools:
    data = json.load(pools)

    parser = []

    for pool in data:
        start_time, end_time = pool['WorkingHoursSummer']['Понедельник'].split('-')
        if datetime.strptime(start_time, '%H:%M') <= datetime(year=1900, month=1, day=1, hour=10) and datetime.strptime(end_time, '%H:%M') >= datetime(year=1900, month=1, day=1, hour=12):
            parser.append(pool)

    parser = sorted(parser, key=lambda params: (params['DimensionsSummer']['Length'], params['DimensionsSummer']['Width']), reverse=True)[0]

    print(f'{parser["DimensionsSummer"]["Length"]}x{parser["DimensionsSummer"]["Width"]}\n'
          f'{parser["Address"]}')
