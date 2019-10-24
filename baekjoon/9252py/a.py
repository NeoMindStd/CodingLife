s1, s2 = input(), input()
dp = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+s1[i-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=lambda x: len(x))
m = ""
for row in dp:
    m = max(row+[m], key=lambda x: len(x))
print(len(m),m,sep='\n')
