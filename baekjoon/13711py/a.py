from bisect import bisect

n = int(input())
s1, s2 = list(map(int, input().split())), list(map(int, input().split()))
s1 = {s1[i]:i for i in range(n)}
s3 = [0]*n
for i in range(n):
    s3[i]=s1[s2[i]]+1
s2 = [0]+s3

dp, ai, di, c = [0]*(n+1), [0]+[n+2]*(n), [0]*(n+1), 0
for i in range(1, n+1):
    if ai[c] < s2[i]:
        dp[i] = di[c]+1
        c+=1
        di[c]=c
        ai[c] = s2[i]
    else:
        idx = bisect(ai, s2[i], lo=0, hi=c+1)-1
        dp[i] = di[idx]+1
        ai[dp[i]] = min(ai[dp[i]], s2[i])

print(c)
