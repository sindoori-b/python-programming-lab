class rect:
    count=0
    def __init__(self,b,l):
        self.b=b
        self.l=l
        rect.count=rect.count+1
    def area(self):
        returnself.b*self.l
    def peri(self):
        return 2*(self.b+self.l)
l1=input("enter the length")
b1=input("enter the breadth")
l2=input("enter the length")
b2=input("enter the breadth")
a=rect(l1,b1)
c=rect(l2,b2)
if a.area==c.area:
    print("equal")
else:
    print("not equal")
