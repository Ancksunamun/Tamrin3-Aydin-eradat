import random

n= int(input("Please enter length of your array:"))
arra = []
while n> 0:


    c=random.randint(1,20)
    if c not in arra:
        arra.append(c)
        n-=1

print (arra)
