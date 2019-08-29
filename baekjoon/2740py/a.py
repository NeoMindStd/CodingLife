n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
_, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for g in range(k):
        tmp = 0
        for j in range(m):
            tmp += a[i][j] * b[j][g]
        print(tmp, end=" ")
    print()
