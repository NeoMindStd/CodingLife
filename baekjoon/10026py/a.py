import sys;read=sys.stdin.readline
import collections

n = int(read())
paint = [list(read()[:-1]) for _ in range(n)]

q = collections.deque([])
enQ = q.append
deQ = q.popleft

def bfs():
    global n, paint
    area = cnt = 0
    visited = [[False]*n for _ in range(n)]
    
    while cnt < n*n:
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = True
                    enQ((i,j))
                    cnt += 1
                    break
            if q: break
        while q:
            i,j = deQ()
            color = paint[i][j]
            if 0<i and not visited[i-1][j] and paint[i-1][j] == color:
                visited[i-1][j] = True
                enQ((i-1,j))
                cnt += 1
            if 0<j and not visited[i][j-1] and paint[i][j-1] == color:
                visited[i][j-1] = True
                enQ((i,j-1))
                cnt += 1
            if n-1>i and not visited[i+1][j] and paint[i+1][j] == color:
                visited[i+1][j] = True
                enQ((i+1,j))
                cnt += 1
            if n-1>j and not visited[i][j+1] and paint[i][j+1] == color:
                visited[i][j+1] = True
                enQ((i,j+1))
                cnt += 1
        area += 1
    return area

a=bfs()
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R': paint[i][j] = 'G'
print(a, bfs())
