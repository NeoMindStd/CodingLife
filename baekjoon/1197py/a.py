import sys;read=sys.stdin.readline
v,e=map(int,read().split())
l=dict()
lines=[list(map(int,read().split()))for _ in range(e)]
for i in range(e):
    lines[i][0]-=1
    lines[i][1]-=1
INT_MAX=2147483648


for line in lines:
    try:l[line[0]]
    except KeyError:l[line[0]]=set()
    l[line[0]].add(line[1])
    try:l[line[1]]
    except KeyError:l[line[1]]=set()
    l[line[1]].add(line[0])

def detectMin(d, c):
    m=INT_MAX
    r=-1
    for i in range(len(d)):
        if m > d[i] and i not in c:
            m = d[i]
            r=i
    if r!=-1: c.add(r)
    return r

def w(u,v):
    for i in range(len(lines)):
        if lines[i][0]==u and lines[i][1]==v or\
        lines[i][0]==v and lines[i][1]==u :
            return lines[i][2]

def prim(r=0):
    global v
    tree=dict()
    d=[INT_MAX for _ in range(v)]
    d[r]=0
    c=set()
    cnt=1
    while len(c)<v:
        u = detectMin(d,c)
        for v in l[u]:
            wuv=w(u,v)
            if v not in c and wuv<d[v]:
                d[v]=wuv
                tree[v]=u
                cnt+=1
    return sum(d)
print(prim())
