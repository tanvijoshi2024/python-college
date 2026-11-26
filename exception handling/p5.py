#raise exception
age=15
try:
    if age< 18:
        raise ValueError("You must be 18 or older")
except ValueError:
    print("minnor")
    
else:
    print("Access granted")