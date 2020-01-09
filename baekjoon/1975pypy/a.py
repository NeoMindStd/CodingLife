import sys;read=sys.stdin.readline
r=[]
for t in range(int(read())):
    n,s=int(read()),0
    for i in range(2,n+1):
        l=[n]
        while True:
            l.append(l[-1]//i)
            l[-2]%=i
            if l[-1]<i:break
        i=0
        while l[i]==0:i+=1
        s+=i
    r.append(s)
print('\n'.join(map(str,r)))
