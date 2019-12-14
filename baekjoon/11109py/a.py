for T in range(int(input())):
    d,n,s,p=map(int,input().split())
    se,pe=n*s,n*p+d
    if se>pe:print('parallelize')
    elif se<pe:print('do not parallelize')
    else:print('does not matter')
