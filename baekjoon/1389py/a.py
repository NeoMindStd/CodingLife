import sys;read=sys.stdin.readline
import collections
n,m=map(int,read().split())
d={}
for i in range(n):
    l=list(map(int,read().split()))
    try:d[l[0]].add((l[1],0))
    except:d[l[0]]=set([(l[1],0)])
    try:d[l[1]].add((l[0],0))
    except:d[l[1]]=set([(l[0],0)])
r={}
for k in d.keys():
    s=set([k])
    q=collections.deque(d[k])
    while q:
        t=q.popleft()
        s.add(t[0])
        try:
            for p in d[t[0]]:
                if p[0] not in s:q.append((p[0],p[1]+1))
        except:continue
        print(k,q)
    r[k]=t[1]
print(list(r.items()))
