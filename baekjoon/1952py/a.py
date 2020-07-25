m,n=map(int,input().split())
a=b=x=y=1
c=0
while True:
    if c%4==0: x+=1
    elif c%4==1: y+=1
    elif c%4==2: x-=1
    else: y-=1
    if not(a<=y<=m) or not(b<=x<=n):
        if c%4==0: a+=1
        elif c%4==1: n-=1
        elif c%4==2: m-=1
        else: b+=1
        if not(a<=m and b<=n):break
        else: c+=1
print(c)
