import sys;read=sys.stdin.readline
h,x=map(int,read().split())
s=0
a=x
for i in range(h):
    s=(s+int(read())*a)%1000000007
    a=(a*x)%1000000007
print(s)
