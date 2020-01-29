while True:
    n=int(input())
    if n==0:break
    a,b,c=map(int,input().split())
    if b<<1==a+c:print(n*(2*a+(n-1)*(b-a))//2)
    else:
        r=b//a
        print(a*(r**n-1)//(r-1))
