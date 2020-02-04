import sys;read=sys.stdin.readline
for T in range(int(read())):
    k,n=map(int,read().split())
    print(k,n*(n+1)//2+n)
