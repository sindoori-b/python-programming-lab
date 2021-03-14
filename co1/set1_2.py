s=int(input("enter a the year"))
print("leap years bw 2021 and ",s)
for i in range(2021,s+1):
    if (i%4==0):
        print(i)
