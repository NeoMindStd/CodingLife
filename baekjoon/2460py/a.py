x = 0
m = 0
for _ in range(10):
    a, b = map(int, input().split())
    x -= a
    m = max(m, x)
    x += b
    m = max(m, x)
print(m)
