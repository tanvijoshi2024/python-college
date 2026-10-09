#accept the name and check if its palindrome
name=(input("enter the name"))
if name==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")

