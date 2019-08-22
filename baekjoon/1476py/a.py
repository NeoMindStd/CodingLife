e, s, m = map(int, input().split())

i = j = k = cnt = 0
while True:
    cnt += 1
    if (i+1, j+1, k+1) == (e, s, m):
        print(cnt)
        break
    i = (i+1)%15
    j = (j+1)%28
    k = (k+1)%19
