color1=input("enter the first list of colors by comma")
color2=input("enter the second list of colors by comma")
c1=set(color1.split(","))
c2=set(color2.split(","))
print("the difference is:",c1.difference(c2))