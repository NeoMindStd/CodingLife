n, m = map(int, input().split())
baskets = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    baskets[a], baskets[b] = baskets[b], baskets[a]
print(*baskets[1:])
