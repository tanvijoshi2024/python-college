#Give a pattern 
# *
# ##
# ***
# ####
n = input("enter the number of rows:")
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    else:
        print("#",end=" ") 

print()