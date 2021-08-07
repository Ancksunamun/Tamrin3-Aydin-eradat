print("plz enter your number in order of lower to higher and type exit for quite")

aray=[]
while True:
    num=input("your number:")

    if num=='exit':

        break
    aray.append(num)

aray_length= len(aray)
k=False
for i in range(aray_length-1):
    if aray[i+1] < aray[i]:
        print("not sorted")
        k=True
if  k is False:
    print("It is sorted good jub")