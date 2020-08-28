import sys; read = sys.stdin.readline
from collections import deque

# 입력
n, m = map(int, read().split())
nums = [list(map(int, read().split())) for _ in range(n)]

# 백트래킹 준비
blocks = set([])
q = deque([[(0,0)]])
enQ = q.append
deQ = q.popleft

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 모양 백트래킹
while q:
    current = deQ()

    for direction in directions:
        for cell in current:
            i, j = cell[0] + direction[0], cell[1] + direction[1]
            if abs(i + j) > 4: continue
            if (i,j) in current: continue
            target = current + [(i,j)]
            if len(target) >= 4:
                blocks.add(tuple(sorted(target)))
                continue
            enQ(target)
#print(blocks)

### 백트래킹 결과 단위 테스트
##for block in blocks:
##    debugPrint = [['.']*7 for _ in range(7)]
##    for cell in block:
##        debugPrint[3+cell[0]][3+cell[1]] = '#'
##    debugPrint2 = []
##    for row in debugPrint: debugPrint2.append(''.join(row))
##    print('\n'.join(debugPrint2))
##    print('--------------')

# 브루트 포스
answer = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            blockSum = 0
            try:
                for cell in block:
                    r, c = i+cell[0], j+cell[1]
                    if not(0 <= r < n) or not(0 <= c < m): raise IndexError
                    blockSum += nums[r][c]
                    #print(i+cell[0], j+cell[1], nums[r][c])
            except IndexError: continue
            answer = max(answer, blockSum)
        #print(answer, blockSum)

print(answer)
