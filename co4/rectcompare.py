class A:
    __length=0
    __width=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__width=w
    def area(self):
        self.__area=self.__length*self.__width
    def __gt__(self,other):
        if(self.__area>other.__area):
            return True
        else:
            return False
rect1=A(3,4)
rect1.area()
rect2=A(6,5)
rect2.area()
if(rect1>rect2):
    print("rect1 is greater than rect2")
else:
    print("rect2 is greater than rect1")