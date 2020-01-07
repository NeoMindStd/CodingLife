for C in range(int(input())):
    s,n,t,l=input().split()
    n,t,l=map(int,[n,t,l])
    if s[2:-1]=='N':r=n*t
    elif s[2:-1]=='N^2':r=n*n*t
    elif s[2:-1]=='N^3':r=n**3*t
    elif s[2:-1]=='2^N':r=2**n*t
    else:
        f=i=1
        while f <=l*10**8 and i <= n:
            f*=i
            i+=1
        r=f*t
    print('TLE!'if r>l*10**8 else'May Pass.')
