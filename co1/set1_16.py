str=input("enter the string")
new=str.split(" ")
a=new[0]
b=new[-1]
print("after swapping first char",b[:1]+a[1:]+' '+a[:1]+b[1:])


