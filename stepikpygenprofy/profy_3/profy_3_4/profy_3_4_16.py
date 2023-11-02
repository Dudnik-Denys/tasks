from datetime import timedelta

hours, minutes, seconds = map(int, input().split(':'))
print(timedelta(hours=hours, minutes=minutes, seconds=seconds).seconds)
