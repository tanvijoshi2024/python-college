#execption stored in an object
age=15
try:
    if age< 18:
        raise ValueError("Minnor")
except ValueError as e:
    print("error:", e)
    
else:
    print("Access granted")