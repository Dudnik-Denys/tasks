from collections import namedtuple
import re


def log_for(logfile: str, date_str: str):
    with (open(logfile, encoding='utf-8') as log_file,
          open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file):
        pattern = namedtuple('Log_line', ['date', 'msg_type', 'msg'])
        regexp = re.compile(r'(\d{4}-\d{2}-\d{2})\s([A-Z]+:)\s(.+)')
        data = [pattern(*re.fullmatch(regexp, line.strip()).groups()) for line in log_file.readlines() if
                re.fullmatch(regexp, line.strip())]
        for line in data:
            file.write(f'{line.msg_type} {line.msg}\n' if line.date == date_str else '')
