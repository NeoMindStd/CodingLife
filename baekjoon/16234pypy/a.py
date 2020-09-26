import sys; read = sys.stdin.readline
from collections import deque

n, l, r = map(int, read().split())
nations = [list(map(int, read().split())) for _ in range(n)]

q = deque([])
enQ = q.append
deQ = q.popleft

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
falseRow = [False] * n

cnt = 0
while True:
    visited = [falseRow.copy() for _ in range(n)]

    unions = []
    sums = []
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            visited[i][j] = True
            union = [(i, j)]
            unionSum = nations[i][j]
            enQ((i, j))
            
            while q:
                cur = deQ()

                for d in directions:
                    nr, nc = cur[0] + d[0], cur[1] + d[1]
                    
                    if 0 <= nr < n and\
                       0 <= nc < n and\
                       not visited[nr][nc] and\
                       l <= abs(nations[cur[0]][cur[1]] - nations[nr][nc]) <= r:
                        visited[nr][nc] = True
                        union.append((nr, nc))
                        unionSum += nations[nr][nc]
                        enQ((nr, nc))

            if len(union) > 1:
                unions.append(union)
                sums.append(unionSum)
            
    if not unions: break
    
    cnt += 1

    for idx in range(len(unions)):
        for i, j in unions[idx]:
            nations[i][j] = sums[idx] // len(unions[idx])

print(cnt)
