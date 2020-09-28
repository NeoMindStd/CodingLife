n, m = map(int, input().split())

baskets = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(lambda x:int(x) - 1, input().split())
    for p in range((j - i) // 2 + 1):
        baskets[i + p], baskets[j - p] = baskets[j - p], baskets[i + p]
print(*baskets)
