#Codeforce 1223A
case=int(input())
for i in range(case):
    matches=int(input())
    if matches==2:
        print("2")
    elif matches%2==0:
        print("0")
    else:
        print("1")
