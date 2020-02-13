import sys;read=sys.stdin.readline

v,e=map(int,read().split())
k=int(read())
d={i:[]for i in range(v)}
V=[300000]*v
V[k-1]=0
Q=set([i for i in range(v)])
for i in range(e):
    x,y,z=map(int,read().split())
    d[x-1].append([y-1,z])
    
def extractMin(Q,V):
    m=300001
    for i in Q:
        if V[i]<m:
            m=V[i]
            index=i
    return index
    
while Q:
    u=extractMin(Q,V)
    Q.remove(u)
    for l in d[u]:
        if l[0] in Q and V[l[0]]>V[u]+l[1]:V[l[0]]=V[u]+l[1]

print('\n'.join(map(lambda x:str(x)if x<300000 else'INF',V)))
