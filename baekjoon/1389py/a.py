import sys;read=sys.stdin.readline
from collections import deque

# 입력
n,m=map(int,read().split())
d=[[0]*n for _ in range(n)] # d[a-1][b-1] = d[b-1][a-1] = a와 b의 친구 단계

for i in range(m):
    a,b=map(int,read().split())
    d[a-1][b-1] = d[b-1][a-1] = 1

# print(d)

# BFS 준비
q=deque([])
enQ=q.append
deQ=q.popleft

# BFS
for i in range(n):
    q.clear()
    visited = [False]*n
    enQ((i,0))
    visited[i] = True
    
    while q:
        j,lv=deQ()
        for k in range(n):
            if not visited[k] and d[j][k] == 1:
                d[i][k] = d[k][i] = lv+d[j][k]
                enQ((k,lv+d[j][k]))
                visited[k] = True
# print(d)

r = list(map(sum,d))
print(r.index(min(r))+1)
