while True:
    n,m,k=map(int,input().split())
    if n==0:break
    print(max(n//2+1-m,0)if n-k>n//2 else-1)
