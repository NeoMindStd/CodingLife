n, k = map(int,input().split())
obj = [list(map(int, input().split())) for _ in range(n)]
obj.sort(key=lambda x:x[1]/x[0])

dp = [0,0]

for i in range(n):
    if dp[0]+obj[i][0] <= k:
        dp=[dp[0]+obj[i][0],dp[1]+obj[i][1]]
print(dp[1])
