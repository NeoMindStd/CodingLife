import sys; read=sys.stdin.readline

n, m, x, y, k = map(int, read().split())
cells = [list(map(int, read().split())) for _ in range(n)]
moves = list(map(int, read().split()))

d = [0]*6

def roll(to):
    global d
    if to == 1: d = [d[0], d[5], d[2], d[4], d[1], d[3]]
    elif to == 2: d = [d[0], d[4], d[2], d[5], d[3], d[1]]
    elif to == 3: d = [d[3], d[0], d[1], d[2], d[4], d[5]]
    elif to == 4: d = [d[1], d[2], d[3], d[0], d[4], d[5]]

i, j = x, y
for move in moves:
    ti, tj = i, j
    if move == 1: tj += 1
    elif move == 2: tj -= 1
    elif move == 3: ti -= 1
    elif move == 4: ti += 1

    if not(0 <= ti < n) or not(0 <= tj < m): continue

    i, j = ti, tj
    roll(move)
    
    if cells[i][j] == 0: cells[i][j] = d[1]
    else: d[1], cells[i][j] = cells[i][j], 0

    print(d[3])
