for T in range(int(input())):
    s=r=0
    for i in range(int(input())):
        a,b=map(float,input().split())
        s+=a
        r+=a*b
    print(int(s),r/s)
