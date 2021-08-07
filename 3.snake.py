
import math
n= int (input("Please enter the length of snake:"))

for i in range (n):
    if (i+1)%2==1:
        print("*",end='')
    else:
        print("#",end='')