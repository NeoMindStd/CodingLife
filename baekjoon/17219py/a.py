import sys;read=sys.stdin.readline
n,m=map(int,read().split())
d,r={},[]
for i in range(n):
    k,v=read().split()
    d[k]=v
for i in range(m):r.append(d[input()])
print('\n'.join(r))
