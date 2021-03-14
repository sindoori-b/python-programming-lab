st=input("enter a string")
s=st.split(" ")
a=list(set(s))
for i in a:
    print(i,"->",s.count(i))