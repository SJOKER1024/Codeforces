#Codeforce 1284A
x,y=(int(v) for v in input().split())
n=[p for p in input().split()]
m=[q for q in input().split()]
case=int(input())
for i in range(case):
    year=int(input())
    print(n[year%x - 1]+m[year%y - 1])
