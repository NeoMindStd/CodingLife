n,m=map(int,input().split())
l=list(map(int,input().split()))
d=1
for i in l:
    d*=i
    d%=m
print(d)
