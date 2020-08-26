import sys; read=sys.stdin.readline
from collections import deque

q = deque([])
enQ = q.append
deQ = q.popleft

ops = ['D', 'S', 'L', 'R']

answer = []

for T in range(int(read())):
    q.clear()
    a,b=map(int,read().split())

    enQ([a,''])
    visited = set([a])

    while q:
        cur = deQ()

        for op in ops:
            tmp = cur.copy()

            if op == 'D': tmp[0] = tmp[0] * 2 % 10000
            elif op == 'S': tmp[0] = (tmp[0] - 1) % 10000
            else:
                st = '%04d'%tmp[0]
                if op == 'L': tmp[0] = int(st[1:] + st[0])
                elif op == 'R': tmp[0] = int(st[-1] + st[:-1])
                    
            if tmp[0] in visited: continue
            tmp[1] += op
            visited.add(tmp[0])
            
            enQ(tmp)
            
            if tmp[0] == b:
                answer.append(tmp[1])
                q.clear()
                break

print('\n'.join(answer))
