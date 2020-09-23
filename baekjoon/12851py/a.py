from collections import deque

MAX_POS = 150_000

n, k = map(int, input().split())

q = deque([(n, 0)])
enQ = q.append
deQ = q.popleft
visited = [MAX_POS]*MAX_POS
visited[n] == 0

answers = [MAX_POS]

while q:
    pos, time = deQ()
    if pos == k: answers.append(time)

    time += 1
    
    if pos * 2 < MAX_POS and visited[pos * 2] >= time <= min(answers):
        visited[pos * 2] = time
        enQ((pos * 2, time))
        
    if pos + 1 < MAX_POS and visited[pos + 1] >= time <= min(answers):
        visited[pos + 1] = time + 1
        enQ((pos + 1, time))
        
    if 0 < pos and visited[pos - 1] >= time <= min(answers):
        visited[pos - 1] = time + 1
        enQ((pos - 1, time))


print(min(answers))
print(len(list(filter(lambda x: x==min(answers), answers))))
