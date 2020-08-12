import collections
import sys;read=sys.stdin.readline

def getDistance(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])

for T in range(int(read())):
    n=int(read())
    h=tuple(map(int,read().split()))
    cs=[tuple(map(int,read().split())) for _ in range(n)]
    p=tuple(map(int,read().split()))
    cs.append(p)

    q=collections.deque([h])
    f=False
    while q:
        cur=q.popleft()
        if cur==p:
            f=True
            break
        for c in cs:
            d = getDistance(cur,c)
            if d <= 1000:
                q.append(c)
                cs.remove(c)
        
    print('happy' if f else 'sad')
