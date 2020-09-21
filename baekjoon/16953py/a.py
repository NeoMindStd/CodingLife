from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])
enQ = q.append
deQ = q.popleft

answer = -1
while q:
    n, cnt = deQ()
    cnt += 1

    if n * 2 == b or n*10 + 1 == b:
        answer = cnt
        break
    if n * 2 < b: enQ((n * 2, cnt))
    if n * 10 + 1 < b: enQ((n * 10 + 1, cnt))
    
print(answer)
