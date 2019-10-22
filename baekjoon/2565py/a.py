n = int(input())

lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort(key = lambda line:line[0])

dp = [0]*n
dp[0] = 1
for i in range(1, n):
    comp = [0]
    for j in range(i):
        if lines[i][1] >= lines[j][1]:
            comp.append(dp[j])
    dp[i] = max(comp)+1
print(n-max(dp))
