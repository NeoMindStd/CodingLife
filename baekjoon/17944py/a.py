a,b=map(int,input().split())
c=0
for i in range(b):
    if c<=1:d=1
    elif c==2*a:d=-1
    c+=d
print(c)
