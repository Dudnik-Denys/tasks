from datetime import datetime, timedelta


def teacher_schedule(start: str, finish: str):
    pattern = '%H:%M'
    start = datetime.strptime(start, pattern)
    finish = datetime.strptime(finish, pattern)
    diff = finish - start
    lesson = timedelta(minutes=45)
    brake = timedelta(minutes=10)
    while start <= finish and diff >= lesson:
        print(f'{start.strftime(pattern)} - {(start + lesson).strftime(pattern)}')
        start = start + lesson + brake
        diff = finish - start


s, f = input(), input()
teacher_schedule(s, f)
