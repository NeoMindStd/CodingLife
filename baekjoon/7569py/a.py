import sys;read=sys.stdin.readline
from collections import deque
m,n,h=map(int,read().split())
# tomatos[h][n][m]
tomatos=[[list(map(int,read().split()))for j in range(n)]for i in range(h)]
Q,d=deque([]),((0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k]==1:Q.append((i,j,k,tomatos[i][j][k]))
while Q:
    i,j,k,c=Q.popleft()
    for move in d:
        mi,mj,mk=i+move[0],j+move[1],k+move[2]
        if 0<=mi<h and 0<=mj<n and 0<=mk<m and tomatos[mi][mj][mk]==0:
            tomatos[mi][mj][mk]=c+1
            Q.append((mi,mj,mk,c+1))
f=False
for floor in tomatos:
    for row in floor:
        for tomato in row:
            if tomato==0:
                f=True
                break
        if f:break
    if f:break
print(-1 if f else c-1)
