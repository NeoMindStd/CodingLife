N, M = tuple(map(int, input().split()))

maze = list()
for i in range(N):
    row = list(map(int, input()))
    maze.append([row[i] for i in range(len(row))])

s = list()
x = y = c = d = 0
s.append((x, y, c, d))
while (x, y) != (N-1, M-1):
    print(x, y, c, d)
    if d > 3:
        x, y, c, d = s.pop()
        d += 1
    c += 1
    if d == 0:
        if y+1 < M:
            y += 1
            if maze[x][y] == 0:
                y -= 1
                d += 1
                c -= 1
                continue
        else:
            d += 1
            c -= 1
            continue
    elif d == 1:
        if x+1 < N:
            x += 1
            if maze[x][y] == 0:
                x -= 1
                d += 1
                c -= 1
                continue
        else:
            d += 1
            c -= 1
            continue
    elif d == 2:
        if y-1 > 0:
            y -= 1
            if maze[x][y] == 0:
                y += 1
                d += 1
                c -= 1
                continue
        else:
            d += 1
            c -= 1
            continue
    elif d == 3:
        if x-1 > 0:
            x -= 1
            if maze[x][y] == 0:
                x += 1
                d += 1
                c -= 1
                continue
        else:
            d += 1
            c -= 1
            continue
    s.append((x, y, c, d))
    d = 0
print(c)
    
