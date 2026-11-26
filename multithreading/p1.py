# ek process ke andar agar multiple threads chal rahe hai usko multithreading bolte hai
import time
def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Teak 2 completed")

task1()
task2()
#sequential execution
#one task starts it complets its process and then the second task starts