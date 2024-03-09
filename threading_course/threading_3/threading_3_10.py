import threading


# mock-functions for test in IDE (change parameters)
executer, logging = lambda: None, lambda: None


def test_thread_timer(t_check: int | float):
    thread = threading.Thread(target=executer, name='Thread', daemon=True)
    thread.start()
    timer = threading.Timer(t_check, logging)
    timer.name = 'Timer'
    timer.start()
    thread.join(t_check + 0.01)
    timer.cancel()
    timer.join()
