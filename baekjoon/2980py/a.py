import sys; read = sys.stdin.readline

n, l = map(int, read().split())
lamps = [list(map(int, read().split()))+[False, 0] for _ in range(n)]

t = s = 0
i = 0
while s < l:
    if i < n and lamps[i][0] == s and lamps[i][4] == 1:
        s += 1
        i += 1
    elif i >= n or lamps[i][0] > s:
        s += 1
    t += 1
    for lamp in lamps:
        lamp[3] += 1
        if lamp[3] >= lamp[lamp[4] + 1]:
            lamp[3] = 0
            lamp[4] = (lamp[4] + 1) % 2
print(t)
