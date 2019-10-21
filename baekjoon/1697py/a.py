from collections import deque

Q = deque([])
enQ = Q.append
deQ = Q.popleft

n, k = map(int, input().split())
enQ((n, 0, set()))

while Q:
    pos = deQ()
    pos[2].add(pos[0])
    if pos[0] == k:
        print(pos[1])
        break
    if pos[0] > 0 and pos[0]-1 not in pos[2]:
        enQ((pos[0]-1, pos[1]+1, pos[2]))
    if pos[0] < 100000 and pos[0]+1 not in pos[2]:
        enQ((pos[0]+1, pos[1]+1, pos[2]))
    if pos[0] <= 50000 and pos[0]*2 not in pos[2]:
        enQ((pos[0]*2, pos[1]+1, pos[2]))
