#Codeforce 59A
str1=input().strip("\n\r")
u,l = 0,0
for i in range(len(str1)):
    if str1[i].isupper() == True:
        u+=1
    else:
        l+=1
if u > l:
    print(str1.upper())
else:
    print(str1.lower())
