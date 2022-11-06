#Codeforce 1220A
x=int(input())
y=input()
one=y.count("n")
zero=(x-one*3)//4
if zero == 0:
    print("1 "*(one-1)+"1")
else:
    print("1 "*one+"0 "*(zero-1)+"0")
