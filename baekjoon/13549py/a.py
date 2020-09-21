from collections import deque

MAX_POS = 101_762

n, k = map(int, input().split())

q = deque([(n, 0)])
push_right = q.append
push_left= q.appendleft
pop = q.popleft
visited = [MAX_POS]*MAX_POS
visited[n] == 0

answers = []

while q:
    pos, time = pop()
    if pos == k: answers.append(time)

    if pos * 2 < MAX_POS and visited[pos * 2] > time:
        visited[pos * 2] = time
        push_left((pos * 2, time))
        
    if pos + 1 < MAX_POS and visited[pos + 1] > time + 1:
        visited[pos + 1] = time + 1
        push_right((pos + 1, time + 1))
        
    if 0 < pos and visited[pos - 1] > time + 1:
        visited[pos - 1] = time + 1
        push_right((pos - 1, time + 1))


print(min(answers))
