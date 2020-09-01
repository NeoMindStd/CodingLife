from collections import deque

n = int(input())
k = int(input())
apples = set([tuple(map(int, input().split())) for _ in range(k)])
l = int(input())
moves = deque(map(lambda x:(int(x[0]), x[1]), [input().split() for _ in range(l)]))
snake = deque([(1,1)])
time = headDir = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, -0)]

while True:
    # 다음 머리 위치
    i = snake[0][0] + directions[headDir][0]
    j = snake[0][1] + directions[headDir][1]

    # 충돌 검사
    if not (0 < i <= n) or\
       not (0 < j <= n) or\
       (i, j) in snake: break

    # 사과를 먹었는지 여부 검사
    if (i, j) in apples: apples.remove((i, j))
    else: snake.pop()

    # 머리 움직임
    snake.appendleft((i, j))

    # 시간 흐름
    time += 1

    # 주어진 방향 변환 정보 반영
    if moves and time >= moves[0][0]:
        if moves[0][1] == 'L': headDir -= 1
        elif moves[0][1] == 'D': headDir += 1
        headDir %= 4
        moves.popleft()
    
print(time + 1)
