import sys; read=sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
cells = [list(map(int, read().split())) for _ in range(n)]

#for row in cells: print(*row)

emptyCells, virusCells = [], []
for i in range(n):
    for j in range(m):
        if cells[i][j] == 0: emptyCells.append((i,j))
        elif cells[i][j] == 2: virusCells.append((i,j))

#print(emptyCells)

wallCases = []

def backTracking(wallCase):
    if len(wallCase) >= 3:
        wallCases.append(wallCase)
        return
    for i in range(wallCase[-1]+1, len(emptyCells)+len(wallCase)-2):
        backTracking(wallCase+[i])

for i in range(len(emptyCells)-2):
    backTracking([i])

#print(wallCases)

virusCellMin = 64

directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]

q = deque([])
enQ = q.append
deQ = q.popleft

for wallCase in wallCases:
    q.clear()
    tmpCells = [cells[i][:] for i in range(n)]
    for virusCell in virusCells: enQ(virusCell)
    for idx in wallCase:
        tmpCells[emptyCells[idx][0]][emptyCells[idx][1]] = 1
    tmpVirusCnt = len(virusCells)

    while q:
        virus = deQ()
        for direction in directions:
            i, j = virus[0] + direction[0], virus[1] + direction[1]
            if 0 <= i < n and\
               0 <= j < m and\
               tmpCells[i][j] == 0:
                tmpCells[i][j] = 2
                enQ((i, j))
                tmpVirusCnt += 1
                if tmpVirusCnt >= virusCellMin:
                    q.clear()
                    break
                
    virusCellMin = min(tmpVirusCnt, virusCellMin)

print(len(emptyCells) - 3 - virusCellMin + len(virusCells))
