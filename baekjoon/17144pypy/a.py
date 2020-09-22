import sys; read = sys.stdin.readline

r, c, t = map(int, read().split())
ap = []
a = []
for i in range(r):
    a.append(list(map(int, read().split())))
    if a[-1][0] == -1:
        ap.append(i)
        a[-1][0] = 0

for dt in range(t):
    na = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                na[i][j] += a[i][j]
                if i > 0 and (i - 1 not in ap or j > 0):
                    na[i - 1][j] += a[i][j] // 5
                    na[i][j] -= a[i][j] // 5
                if i < r - 1 and (i + 1 not in ap or j > 0):
                    na[i + 1][j] += a[i][j] // 5
                    na[i][j] -= a[i][j] // 5
                if j > 0 and (i not in ap or j - 1 > 0):
                    na[i][j - 1] += a[i][j] // 5
                    na[i][j] -= a[i][j] // 5
                if j < c - 1:
                    na[i][j + 1] += a[i][j] // 5
                    na[i][j] -= a[i][j] // 5
    a = na

    for i in range(ap[0] - 1, 0, -1): a[i][0] = a[i - 1][0]
    for j in range(c - 1): a[0][j] = a[0][j + 1]
    for i in range(ap[0]): a[i][c - 1] = a[i + 1][c - 1]
    for j in range(c - 1, 1, -1): a[ap[0]][j] = a[ap[0]][j - 1]
    a[ap[0]][1] = 0

    for i in range(ap[1] + 1, r - 1): a[i][0] = a[i + 1][0]
    for j in range(c - 1): a[r - 1][j] = a[r - 1][j + 1]
    for i in range(r - 1, ap[1], -1): a[i][c - 1] = a[i - 1][c - 1]
    for j in range(c - 1, 1, -1): a[ap[1]][j] = a[ap[1]][j - 1]
    a[ap[1]][1] = 0

print(sum(map(lambda x: sum(x), a)))
