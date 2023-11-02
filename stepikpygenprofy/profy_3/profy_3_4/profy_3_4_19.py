from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
data = datetime.strptime(input(), pattern)
print(data.strftime(pattern))

for d in range(2, 11):
    td = timedelta(days=d)
    data = data + td
    print(data.strftime(pattern))
