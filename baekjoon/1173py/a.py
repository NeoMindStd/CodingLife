N,m,M,T,R=map(int,input().split())
t,c=0,m
while m+T<=M and N>0:
    t+=1
    if c+T<=M:
        N-=1
        c=min(c+T,M)
    else:c=max(m,c-R)
print(t if t>0 else -1)
