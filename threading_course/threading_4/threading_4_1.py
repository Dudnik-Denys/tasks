import re
import threading
import time


class ReplaceThread(threading.Thread):
    def __init__(self, file: str):
        super().__init__()
        self._file = file
        name, suf = self._file.rsplit('.')
        self._new_file = f'{name}_new.{suf}'
        self._pattern = re.compile(r'a[^a]*n[^n]*t[^t]*o[^o]*n.*', re.I)

    def run(self):
        with open(self._file, encoding='utf-8') as source, open(self._new_file, 'w', encoding='utf-8') as store:
            for line in source:
                store.write('!!! WARNING INFECTED !!!\n' if re.search(self._pattern, line) else line)


start_time = time.monotonic()

# Threading case

threads = [ReplaceThread(f'words_{i}.txt') for i in range(5)]
for thread in threads:
    thread.start()
    thread.join()

print('Total executed time with threading:', time.monotonic() - start_time)  # 0.009021874982863665 - 5

# Only MainThread case

# pattern = re.compile(r'a[^a]*n[^n]*t[^t]*o[^o]*n.*', re.I)
#
# for i in range(5):
#     file = f'words_{i}.txt'
#     name, suf = file.rsplit('.')
#     with open(file, encoding='utf-8') as source, open(f'{name}_new.{suf}', 'w', encoding='utf-8') as store:
#         for line in source:
#             store.write('!!! WARNING INFECTED !!!\n' if re.search(pattern, line) else line)
#
# print('Total executed time without threading:', time.monotonic() - start_time)  # 0.008342624874785542
