from collections import deque

def rotate(gear, direction):
    if direction == 1: gear.appendleft(gear.pop())
    else: gear.append(gear.popleft())

gears = [deque(map(int, input())) for _ in range(4)]

right, left = 2, 6

for i in range(int(input())):
    idx, direction = map(int, input().split())

    targets = [(gears[idx-1], direction)]

    tmpIdx, tmpDir = idx - 2, -direction
    while tmpIdx >= 0:
        if gears[tmpIdx][right] == gears[tmpIdx + 1][left]: break
        targets.append((gears[tmpIdx], tmpDir))
        tmpIdx -= 1
        tmpDir *= -1

    tmpIdx, tmpDir = idx, -direction
    while tmpIdx < 4:
        if gears[tmpIdx - 1][right] == gears[tmpIdx][left]: break
        targets.append((gears[tmpIdx], tmpDir))
        tmpIdx += 1
        tmpDir *= -1

    for target in targets: rotate(*target)

score = 0
for i in range(4): score += gears[i][0]*2**i

print(score)
