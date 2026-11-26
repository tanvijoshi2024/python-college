
try:
    num=int(input("enter a number: "))
    result= 100/num
    print("The quotient of number is: ", result)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("you cannot divide by zero")
