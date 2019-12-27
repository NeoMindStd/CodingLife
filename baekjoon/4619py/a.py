while True:
    b,n=map(int,input().split())
    if n==0:break
    a1=int(b**(1/n))
    a2=a1+1
    an1,an2=a1**n,a2**n
    print(a1 if abs(b-an1)<abs(b-an2)else a2)
