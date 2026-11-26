# multithreading with arguments
import threading

def greet(name):
       print("Hello", name)
       print(name, "Hello")
    
t1=threading.Thread(target=greet, args=("Arav",))

t1.start()
t1.join()


