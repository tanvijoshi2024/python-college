# multithreading with arguments
import threading

def greet(name,age):
       print("Hello", name)
       print("this is age", age)
    
t1=threading.Thread(target=greet,args=("Arav",15) )

t1.start()
t1.join()