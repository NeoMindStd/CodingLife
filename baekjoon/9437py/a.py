while True:
    n=input()
    if n=='0':break
    n,p=map(int,n.split())
    t=p+(1 if p%2!=0 else-1)
    print(*sorted((t,n-p+1,n-t+1)))
