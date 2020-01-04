import sys;read=sys.stdin.readline
n,m=map(int,read().split())
l=[list(map(int,list(input())))for _ in range(n)]
r=1
for t in range(1,min(n,m)):
    for i in range(n-t):
        for j in range(m-t):
            if l[i][j]==l[i+t][j]==l[i][j+t]==l[i+t][j+t]:r=max(r,(t+1)**2)
print(r)
