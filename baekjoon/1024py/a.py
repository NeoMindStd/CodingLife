n,l=map(int,input().split())
while l <= 100:
    if l%2==0:
        a=n//l-l//2+1
        b=n//l+l//2
    else:
        a=n//l-l//2
        b=n//l+l//2
    if b*b+b+a-a*a==2*n:break
    l+=1
try:
    if a<0 or b<0 or b*b+b+a-a*a!=2*n:raise Exception
    print(*[i for i in range(a,b+1)])
except:print(-1)
