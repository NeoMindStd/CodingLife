n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]

info=[[],[],[]]
for i in range(n):
    for j in range(n): info[l[i][j]].append((i,j))

def search(t,d,g):
    if d>=m or t[-1]>=len(info[2])-1 :
        g.append(t)
        return
    g.append(t)
    for i in range(t[-1]+1,len(info[2])): search(t+[i],d+1,g)

g=[]
for i in range(len(info[2])):search([i],1,g)

def calc(t):
    s=0
    for h in info[1]:
        diff=n*n
        for idx in t:
            c = info[2][idx]
            diff = min(diff,abs(c[0]-h[0])+abs(c[1]-h[1]))
        s += diff
    return s

ans=[]
for case in g:
    ans.append(calc(case))
print(min(ans))
