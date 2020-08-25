import sys;read=sys.stdin.readline
n,m=map(int,read().split())
l=[list(map(int,read().split())) for _ in range(n)]
ans=[]
for k in range(int(read())):
    i,j,x,y = map(int,read().split())

    s=0
    for r in range(i-1,x):
        for c in range(j-1,y):s+=l[r][c]
    ans.append(s)
print('\n'.join(map(str,ans)))
