import sys;read=sys.stdin.readline
import collections
_,m=map(int,read().split())
d={}
for i in range(m):
    a,b=map(int,read().split())
    try:d[a].append((b,1))
    except:d[a]=[(b,1)]
    try:d[b].append((a,1))
    except:d[b]=[(a,1)]
r={}
for k in d.keys():
    s=set([k]+[link[0]for link in d[k]])
    q=collections.deque(d[k])
    while q:
        t=q.popleft()
        print(k,t,s)
        try:r[k]+=t[1]
        except:r[k]=t[1]
        for p in d[t[0]]:
            if p[0] not in s:
                q.append((p[0],p[1]+t[1]))
                s.add(p[0])
print(min(r.items(),key=lambda x:(x[1],x[0]))[0])
print(r.items())
