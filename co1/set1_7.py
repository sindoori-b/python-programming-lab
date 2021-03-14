a=[1,56,4,8,7,6]
b=[5,89,6,7,3,1,6]
if(len(a)==len(b)):
    print("same length")
else:
    print("not same length")
    c=0
for i in a:
    c=c+i
c1=0
for i in b:
    c1=c1+i
if c==c1:
    print("sum is equal")
else:
    print("sum isnt equal")
for i in a:
    for j in b:
        if i==j:
            print(i,"is present in both lists")