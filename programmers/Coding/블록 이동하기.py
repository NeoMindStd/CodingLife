from collections import deque

def solution(board):    
    n = len(board)
    
    q = deque([((0, 0), (0, 1), 0)])
    enQ = q.append
    deQ = q.popleft
    visited = set([q[0][:-1]])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        a, b, t = deQ()
        if b[0] == b[1] == n-1: return t
        for d in directions:
            try:
                na, nb = (a[0]+d[0], a[1]+d[1]), (b[0]+d[0], b[1]+d[1])
                if -1 in [*na, *nb]: raise IndexError
                if a > b: a, b = b, a
                
                if board[na[0]][na[1]] == board[nb[0]][nb[1]] != 1 and\
                   (na, nb) not in visited:
                    enQ((na, nb, t+1))
                    visited.add((na, nb))
                    
            except IndexError: continue

        if a[0] == b[0] < n-1:
            is_rotatable = True
            for i in range(2):
                for j in range(2):
                    is_rotatable &= board[a[0]+i][a[1]+j] != 1
            if is_rotatable:
                for c in [a, b]:
                    na, nb = c, (c[0]+1, c[1])
                    if (na, nb) not in visited:
                        enQ((na, nb, t+1))
                        visited.add((na, nb))


        if a[0] == b[0] > 0:
            is_rotatable = True
            for i in range(2):
                for j in range(2):
                    is_rotatable &= board[a[0]-i][a[1]+j] != 1
            if is_rotatable:
                for c in [a, b]:
                    na, nb = (c[0]-1, c[1]), c
                    if (na, nb) not in visited:
                        enQ((na, nb, t+1))
                        visited.add((na, nb))
                    
        if a[1] == b[1] < n-1:
            is_rotatable = True
            for i in range(2):
                for j in range(2):
                    is_rotatable &= board[a[0]+i][a[1]+j] != 1
            if is_rotatable:
                for c in [a, b]:
                    na, nb = c, (c[0], c[1]+1)
                    if (na, nb) not in visited:
                        enQ((na, nb, t+1))
                        visited.add((na, nb))
                        
        if a[1] == b[1] > 0:
            is_rotatable = True
            for i in range(2):
                for j in range(2):
                    is_rotatable &= board[a[0]+i][a[1]-j] != 1
            if is_rotatable:
                for c in [a, b]:
                    na, nb = (c[0], c[1]-1), c
                    if (na, nb) not in visited:
                        enQ((na, nb, t+1))
                        visited.add((na, nb))

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
