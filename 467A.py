#Codeforce 467A
room=int(input())
ans=0
for i in range(room):
    p,q=(int(v) for v in input().split())
    if q - p >= 2:
        ans+=1
print(ans)
