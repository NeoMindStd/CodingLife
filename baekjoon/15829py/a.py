import sys;read=sys.stdin.readline
n,r,m=int(read()),1,1234567891
l=list(map(lambda x:ord(x)-ord('a')+1,read()[:-1]))
for i in range(n):
    l[i]=l[i]*r
    r=r*31%m
print(sum(l)%m)
