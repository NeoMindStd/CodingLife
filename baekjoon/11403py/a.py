import sys;read=sys.stdin.readline
import collections
n=int(read())
d={}
for i in range(n):
    l=list(map(int,read().split()))
    for j in range(n):
        if l[j]>0:
            try:d[i].append(j)
            except:d[i]=[j]

r=[[0]*n for _ in range(n)]
for k,v in d.items():
    q=collections.deque(v)
    while q:
        t=q.popleft()
        r[k][t]=1
        try:
            for p in d[t]:
                if r[k][p]<1:q.append(p)
        except:continue
print('\n'.join(map(lambda x:' '.join(map(str,x)),r)))
