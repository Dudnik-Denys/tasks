from datetime import datetime, timedelta

hours, minutes, seconds = map(int, input().split(':'))
timer = int(input())
t1 = timedelta(hours=hours, minutes=minutes, seconds=seconds)
t2 = timedelta(seconds=timer)
t = str(t1 + t2)
t = t.split(' ')[-1]
print(datetime.strftime(datetime.strptime(t, '%H:%M:%S'), '%H:%M:%S'))


# from datetime import datetime, timedelta
#
# pattern = '%H:%M:%S'
# dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))
#
# print(dt.strftime(pattern))
