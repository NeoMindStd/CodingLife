import sys;read=sys.stdin.readline
for T in range(int(read())):
    k,r=int(read()),0
    i=it=1
    while it<k and r==0:
        j=jt=1
        while it+jt<k and r==0:
            x=k-it-jt
            n=int(1+8*x)**.5//2
            if n*(n+1)//2==x!=0:r=1
            j+=1
            jt=j*(j+1)//2
        i+=1
        it=i*(i+1)//2
    print(r)
