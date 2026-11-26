import threading
import time
def greet():
        print("Start")
        time.sleep(2)
        print("end")
    
def greet2():
    print("Hello from the thread2")

def greet3():
   print("Hello from the thread3")
    

t1=threading.Thread(target=greet)
t2=threading.Thread(target=greet2)
t3=threading.Thread(target=greet3)
t1.start()
t2.start()
t3.start()
