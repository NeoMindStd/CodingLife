import math
for t in range(int(input())):
    n,a,b=map(int,input().split())
    c=math.floor(math.log(a)/math.log(2))
    d=math.floor(math.log(b)/math.log(2))
    while a>0:
        if a>=2**c:a-=2**c
        c-=1
    while b>0:
        if b>=2**d:b-=2**d
        d-=1
    print(n-min(c,d)-1)
