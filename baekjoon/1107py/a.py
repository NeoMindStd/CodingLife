n,m=int(input()),int(input())
btns=set([])
if m>0:btns=set(input().split())

m=abs(n-100)
b=n+100
for i in range(10_000_001):
    f=True
    for c in str(i):f&=c not in btns
    d=len(str(i))+abs(n-i)
    if f and m>d:
        b=m
        m=d
    elif b-d<0:break

print(m)
