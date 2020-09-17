import sys; read = sys.stdin.readline

for T in range(int(read())):
    n = int(read())
    stickers = [list(map(int, read().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if n > 0:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

        for j in range(2, n):
            for i in range(2):
                dp[i][j] = max(stickers[i][j] + dp[(i+1)%2][j-2],
                               stickers[i][j] + dp[i][j-2],
                               stickers[i][j] + dp[(i+1)%2][j-1],
                               dp[i][j-1])
    print(max(dp[0][-1], dp[1][-1]))
