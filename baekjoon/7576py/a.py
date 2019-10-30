from collections import deque
from sys import stdin

m, n = map(int, input().split())
tomatos = [list(map(int, stdin.readline().split())) for _ in range(n)]

Q = deque([])
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            Q.append((i, j, 0))

days = 0
while Q:
    tmp = Q.popleft()
    if tmp[0] > 0 and tomatos[tmp[0]-1][tmp[1]] == 0:
        Q.append((tmp[0]-1, tmp[1], tmp[2]+1))
        tomatos[tmp[0]-1][tmp[1]] = 1
    if tmp[1] > 0 and tomatos[tmp[0]][tmp[1]-1] == 0:
        Q.append((tmp[0], tmp[1]-1, tmp[2]+1))
        tomatos[tmp[0]][tmp[1]-1] = 1
    if tmp[0] < n-1 and tomatos[tmp[0]+1][tmp[1]] == 0:
        Q.append((tmp[0]+1, tmp[1], tmp[2]+1))
        tomatos[tmp[0]+1][tmp[1]] = 1
    if tmp[1] < m-1 and tomatos[tmp[0]][tmp[1]+1] == 0:
        Q.append((tmp[0], tmp[1]+1, tmp[2]+1))
        tomatos[tmp[0]][tmp[1]+1] = 1
    days = tmp[2]

flag = True
for row in tomatos:
    for tomato in row:
        if tomato == 0:
            flag = False
            break
    if not flag:
        break
    
print(days if flag else -1)
