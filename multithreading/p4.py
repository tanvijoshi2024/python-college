import threading
import time
def greet():
       print("Hello from the thread1")
    
def greet2():
    time.sleep(5)
    print("Hello from the thread2")
    

def greet3():
   print("Hello from the thread3")
    

t1=threading.Thread(target=greet)
t2=threading.Thread(target=greet2)
t3=threading.Thread(target=greet3)
t1.start()
t1.join()
t2.start()
t3.start()

print("main program ended")