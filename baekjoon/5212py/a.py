r, c = map(int, input().split())

maps = [list(input()) for _ in range(r)]

new_maps = []
for row in maps: new_maps.append(row.copy())

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(r):
    for j in range(c):
        if new_maps[i][j] == '.': continue
        cnt = 0

        for d in ds:
            ni, nj = i + d[0], j + d[1]
            if not(0 <= ni < r) or\
               not(0 <= nj < c) or\
               maps[ni][nj] == '.':
                cnt += 1

        if cnt >= 3: new_maps[i][j] = '.'

sr = sc = 0
er, ec = r, c

for _ in range(10):
    if new_maps[sr][sc:ec].count('X') < 1: sr += 1
    if list(map(lambda row: row[sc], new_maps[sr:er])).count('X') < 1: sc += 1
    if new_maps[er - 1][sc:ec].count('X') < 1: er -= 1
    if list(map(lambda row: row[ec - 1], new_maps[sr:er])).count('X') < 1: ec -= 1

for i in range(sr, er):
    print(''.join(new_maps[i][sc:ec]))
