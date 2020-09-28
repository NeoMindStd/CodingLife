# 한화의~ 김성근~ 감 독 님 사 랑해~
import sys; read = sys.stdin.readline
import math

result = []
for T in range(int(read())):
    n, m = map(int, read().split())
    teams = {i:[0, 0] for i in range(1, n + 1)}

    for _ in range(m):
        a, b, p, q = map(int, read().split())
        teams[a][0] += p
        teams[a][1] += q
        teams[b][0] += q
        teams[b][1] += p
        
    pes = [((teams[i][0] ** 2 / (teams[i][0] ** 2 + teams[i][1] ** 2))
            if teams[i][0] + teams[i][1] > 0
            else 0) for i in range(1, n + 1)]
            
    result.append(math.floor(max(pes) * 1000))
    result.append(math.floor(min(pes) * 1000))

print('\n'.join(map(str, result)))
