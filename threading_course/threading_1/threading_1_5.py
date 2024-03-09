import threading

tasks = [lambda: print('func'), lambda: print('func'), lambda: print('func')]

for func in tasks:
    threading.Thread(target=func).start()
