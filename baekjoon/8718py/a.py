x,k=map(lambda n:int(n)*1000,input().split())
a=0
for i in [7*k//4,7*k//2,7*k]:
    if i<=x:
        a=i
print(a)
