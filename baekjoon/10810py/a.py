n, m = map(int, input().split())
baskets = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    
    for idx in range(i, j + 1): baskets[idx] = k
    
print(*baskets[1:])
