import sys;read=sys.stdin.readline
k,n=map(int,read().split())
l=[int(read())for _ in range(k)]
a,b,r=1,max(l),0
while True:
    m=(a+b)//2
    s=0
    for i in l:s+=i//m
    if s<n:b=m-1
    else:
        r=max(r,m)
        a=m+1
    if a>b:break
print(r)
