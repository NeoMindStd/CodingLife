import sys; read = sys.stdin.readline

n, m = map(int, read().split())
a = [int(read()) for _ in range(n)]
b = [int(read()) for _ in range(m)]
votes = [0] * n

for max_cost in b:
    for i in range(n):
        if a[i] <= max_cost:
            votes[i] += 1
            break
print(votes.index(max(votes)) + 1)
