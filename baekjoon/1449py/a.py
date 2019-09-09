n, l = map(int, input().split())

pl = list(map(int, input().split()))

pl.sort()

cnt = 0

tmp = 0
for p in pl:
    if tmp < p:
        cnt += 1
        tmp = p + l - 1

print(cnt)
