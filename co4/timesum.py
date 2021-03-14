class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__seconds=s
    def time(self):
        if self.__seconds>=60:
            self.__seconds-=60
            self.__minute+=1
        if self.__minute>=60:
            self.__minute-=60
            self.__hour+=1
    def __add__(self,other):
        self.__hour=self.__hour+other.__hour
        self.__minute=self.__minute+other.__minute
        self.__seconds=self.__seconds+other.__seconds
        return(self.__hour,self.__minute,self.__seconds)

obj1=Time(3,60,60)
obj1.time()
obj2=Time(6,30,5)
obj2.time()
print("Sum of two time:")
print(obj1+obj2)