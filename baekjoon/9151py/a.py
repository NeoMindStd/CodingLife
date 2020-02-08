def e3(n):
    a=int(n**(1/3))
    if (a+1)**3<=n:a+=1
    return a
while True:
    n=int(input())
    if n==0:break
    a=e3(n)
    b=e3(6*n)
    m=0
    for i in range(a+1):
        for j in range(b+1):
            t=i**3+j*(j+1)*(j+2)//6
            if t<=n:m=max(m,t)
    print(m)
