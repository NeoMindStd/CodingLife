n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    row = []
    for j in range(m): row.append(a[i][j]+b[i][j])
    print(*row)
