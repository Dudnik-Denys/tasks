import threading

test = lambda: print('x')

thr = threading.Thread(target=test)
thr.start()
thr.join()
