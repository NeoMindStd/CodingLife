n, p = int(input()), [0]+list(map(int, input().split()))
dp = [0, p[1]]

for i in range(2, n+1):
    ds = []
    for j in range(i//2, i):
        ds.append(dp[j]+dp[i-j])
    dp.append(max([p[i]]+ds))
print(dp[n])
