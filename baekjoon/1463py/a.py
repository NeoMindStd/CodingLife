n = int(input())

cnt = [100000 for _ in range(n+1)]
cnt[1] = 0

for i in range(1, n):
    if i*3 <= n:
        cnt[i*3] = min(cnt[i*3], cnt[i]+1)
    if i*2 <= n:
        cnt[i*2] = min(cnt[i*2], cnt[i]+1)
    cnt[i+1] = min(cnt[i+1], cnt[i]+1)
    
print(cnt[n])
