# two threads
from threading import Thread
import time

def numbers():
    for i in range(1,6):
        print(i)
        time.sleep(2)

def alphabets():
    for ch in ['A',' B',' C' ,'D',' E',' F']:
        print(ch)
        time.sleep(4)

t1=Thread(target=numbers)
t2= Thread(target=alphabets)

t1.start()
t2.start()

t1.join()
t2.join()

print("Task finished")
