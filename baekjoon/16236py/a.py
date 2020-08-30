import sys; read=sys.stdin.readline
import collections

n = int(read())
fishes = [list(map(int, read().split())) for _ in range(n)]

q = collections.deque([])
enQ = q.append
deQ = q.popleft

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i in range(n):
    for j in range(n):
        if fishes[i][j] == 9:
            fishes[i][j] = 0
            shark = (i, j, 0)

size, eat, time = 2, 0, 0
while shark != (-1, -1, -1):
    q.clear()
    enQ(shark)

    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True

##    print('=======')
##    print(f'size: {size}, eat: {eat}, time: {time}, last eat: {shark}')
##    for row in fishes:
##        print(*row)
##    print('=======')

    shark = (-1, -1, -1)

    eatInfo = (-1, -1, 999_999)

    while q:
        current = deQ()
        for direction in directions:
            i, j, dt = current[0] + direction[0], current[1] + direction[1], current[2] + 1

            if not(0 <= i < n) or not(0 <= j < n) or\
               dt > eatInfo[2] or visited[i][j]: continue

            if 0 <= fishes[i][j] <= size:
                if 0 < fishes[i][j] < size:
                    if dt < eatInfo[2] or\
                       eatInfo[0] > i or\
                       (eatInfo[0] == i and eatInfo[1] > j):
                        eatInfo = (i, j, dt)
                else:
                    enQ((i, j, dt))
                    visited[i][j] = True
    if eatInfo[0] > -1 and eatInfo[1] > -1:
        i, j, time = eatInfo[0], eatInfo[1], time + eatInfo[2]
        shark = (i, j, 0)
        fishes[i][j] = 0
        eat += 1
        if eat == size:
            size += 1
            eat = 0

print(time)
