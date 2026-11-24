# simple program
from threading import Thread
def task():
    print("the thread is running")
t=Thread(target=task)
t.start()
t.join()
print("Main program ends")