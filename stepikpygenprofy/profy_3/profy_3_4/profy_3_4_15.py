from datetime import date, timedelta

pattern = '%d.%m.%Y'
data = input().split('.')
data[0], data[2] = data[2], data[0]
data = '-'.join(data)
data = date.fromisoformat(data)
past = date.strftime(data - timedelta(days=1), pattern)
future = date.strftime(data + timedelta(days=1), pattern)
print(past, future, sep='\n')


# from datetime import datetime, timedelta
#
# pattern, td = '%d.%m.%Y', timedelta(days=1)
#
# dt = datetime.strptime(input(), pattern)
#
# print((dt - td).strftime(pattern))
# print((dt + td).strftime(pattern))
