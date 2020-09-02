import sys; read=sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
r, c, d = map(int, read().split())
cells = [list(map(int, read().split())) for _ in range(n)]

directions = [(-1,0), (0,1), (1,0), (0,-1)]

cnt = 0
while True:
    if cells[r][c] == 0: cnt += 1
    cells[r][c] = 2
##    print('=======')
##    print(r,c,d)
##    for row in cells:print(*row)
##    print('=======')
    moved = False
    od = d
    while True:
        d = (d-1) % 4
        i, j = r + directions[d][0], c + directions[d][1]
        if 0 <= i < n and\
           0 <= j < m and\
           cells[i][j] == 0:
            r, c = i, j
            moved = True
            break
        if od == d:break
    #if cells[r][c] != 2:
    if not moved:
        i, j = r + directions[(d+2)%4][0], c + directions[(d+2)%4][1]
        if 0 <= i < n and\
           0 <= j < m and\
           cells[i][j] != 1:
            r, c = i, j
        else: break
        
print(cnt)
