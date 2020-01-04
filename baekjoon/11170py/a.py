for T in range(int(input())):
    n,m=map(int,input().split())
    a=0
    for i in range(n,m+1):
        for c in str(i):
            if c=='0':a+=1
    print(a)
