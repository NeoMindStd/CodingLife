import sys
for line in sys.stdin:
    n,k=map(int,line.split())
    t=n
    while t>=k:
        n+=t//k
        t=t//k+t%k
    print(n)
