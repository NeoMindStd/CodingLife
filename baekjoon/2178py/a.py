import collections

n, m = map(int, input().split())
maze = [[0]*(m+2)]
for _ in range(n):
    maze.append([0]+list(map(int, " ".join(map(str, input())).split()))+[0])
maze += [[0]*(m+2)]

Q = collections.deque([])
deQ = Q.popleft
enQ = Q.append

visitFlag = [[False]*(m+2) for  _ in range(n+2)]

class Pos:
    def  __init__(self, r, c, d, cnt):
        self.r = r
        self.c = c
        self.d = d
        self.cnt = cnt

visitFlag[1][1] = True
enQ(Pos(1, 1, 0, 1))

while Q:
    pos = deQ()
    if pos.r == n and pos.c == m:
        print(pos.cnt)
        break
    cnt = 0
    while cnt < 4:
        if pos.d == 0: 
            if(maze[pos.r-1][pos.c] == 1 and
               not visitFlag[pos.r-1][pos.c]):
                enQ(Pos(pos.r-1, pos.c, 0, pos.cnt+1))
                visitFlag[pos.r-1][pos.c] = True
        elif pos.d == 1:
            if(maze[pos.r][pos.c+1] == 1 and
               not visitFlag[pos.r][pos.c+1]):
                enQ(Pos(pos.r, pos.c+1, 0, pos.cnt+1))
                visitFlag[pos.r][pos.c+1] = True
        elif pos.d == 2:
            if(maze[pos.r+1][pos.c] == 1 and
               not visitFlag[pos.r+1][pos.c]):
                enQ(Pos(pos.r+1, pos.c, 0, pos.cnt+1))
                visitFlag[pos.r+1][pos.c] = True
        else:
            if(maze[pos.r][pos.c-1] == 1 and
               not visitFlag[pos.r][pos.c-1]):
                enQ(Pos(pos.r, pos.c-1, 0, pos.cnt+1))
                visitFlag[pos.r][pos.c-1] = True
        pos.d = (pos.d+1)%4
        cnt += 1
