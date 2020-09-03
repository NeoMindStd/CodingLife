n, m = map(int, input().split())
cells = [list(map(int, input().split())) for _ in range(n)]

infos = [[] for _ in range(7)]
for i in range(n):
    for j in range(m):
        infos[cells[i][j]].append((i, j))

##for row in infos: print(row)

cases = {}

def backTracking(camType, case):
    if len(case) >= len(infos[camType]):
        cases[camType].append(case)
        return
    
    if camType == 5: backTracking(camType, case+[0])
    elif camType == 2:
        backTracking(camType, case+[0])
        backTracking(camType, case+[1])
    else:
        for i in range(4): backTracking(camType, case+[i])

for i in range(1,6):
    if len(infos[i]) > 0:
        cases[i] = []
        backTracking(i, [])

##for key, value in cases.items(): print(key, value)

combs = []
def getCombs(depth, comb):
    if depth == 5:
        combs.append(comb)
        return
    try:
        for i in range(len(cases[depth+1])): getCombs(depth+1, comb+[i])
    except KeyError: getCombs(depth+1, comb+[-1])

getCombs(0, [-1])

def setToWatched(cells, direction, diff):
    if not(0 <= r+direction[0]*diff < n) or\
       not(0 <= c+direction[1]*diff < m) or\
       cells[r+direction[0]*diff][c+direction[1]*diff] == 6: return
    if cells[r+direction[0]*diff][c+direction[1]*diff] == 0:
        cells[r+direction[0]*diff][c+direction[1]*diff] = '#'
    setToWatched(cells, direction, diff+1)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
minBlinds = 64

for comb in combs:
    tmpCells = [cells[i].copy() for i in range(n)]
##    for row in tmpCells: print(row)
    for i in range(1,6):
        for j in range(len(infos[i])):
            r, c = infos[i][j][0], infos[i][j][1]
            if i == 5:
                for direction in directions: setToWatched(tmpCells, direction, 1)
            elif i == 2:
                setToWatched(tmpCells, directions[cases[i][comb[i]][j]], 1)
                setToWatched(tmpCells, directions[cases[i][comb[i]][j]+2], 1)
            else:
                setToWatched(tmpCells, directions[cases[i][comb[i]][j]], 1)
                if i > 1: setToWatched(tmpCells, directions[(cases[i][comb[i]][j]+1)%4], 1)
                if i > 3: setToWatched(tmpCells, directions[(cases[i][comb[i]][j]+2)%4], 1)

    blinds = 0
    for row in tmpCells: blinds += row.count(0)

    minBlinds = min(minBlinds, blinds)

##    print('=====================')
##    print(comb)
##    for row in tmpCells: print(*row)
##    print('=====================')
    
print(minBlinds)
