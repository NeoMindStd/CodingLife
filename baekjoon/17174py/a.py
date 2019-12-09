n,m=map(int,input().split())
s=0
while n > 0:
    s+=n
    n//=m
print(s)
