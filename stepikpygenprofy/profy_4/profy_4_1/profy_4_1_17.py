from datetime import datetime
import sys

dates = [datetime.strptime(dt.strip(), '%d.%m.%Y') for dt in sys.stdin]

if len(dates) != len(set(dates)):
    print('MIX')
elif dates == sorted(dates):
    print('ASC')
elif dates == sorted(dates, reverse=True):
    print('DESC')
else:
    print('MIX')
