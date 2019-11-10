n,m,k=map(int,input().split())
while k>0:
    k-=1
    if n/2>m:n-=1
    else:m-=1
print(min(m,n//2))
