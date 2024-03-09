import threading
from time import sleep


def user_interface():
    while True:
        sleep(0.2)
        print("-", end="")


def task():
    while True:
        sleep(0.61)
        print("*", end="")


threading.Thread(target=task).start()
user_interface()
