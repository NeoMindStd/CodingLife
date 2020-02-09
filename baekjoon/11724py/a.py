import sys;read=sys.stdin.readline
sys.setrecursionlimit(10000)
n,m=map(int,read().split())
d={i+1:set([])for i in range(n)}
for i in range(m):
    u,v=map(int,read().split())
    d[u].add(v)
    d[v].add(u)
s,c=set([]),0
def dfs(u):
    global s,d
    s.add(u)
    for v in d[u]:
        if v not in s:dfs(v)
for key,val in d.items():
    if key in s:continue
    c+=1
    dfs(key)
print(c)
