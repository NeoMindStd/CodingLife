import sys;read=sys.stdin.readline
n,m=int(input()),int(read())
r=0
for i in range(n):
    a,b=map(int,input().split())
    m+=a-b
    if m<0:r=0;break
    r=max(r,m)
print(r)
