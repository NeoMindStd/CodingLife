d = list(map(int, input().split()))


b = (d[0] + d[2] - d[1]) / 2
a = d[0] - b
c = d[2] - b

if min(a, b, c) > 0:
    print(1)
    print(a, b, c)
else:
    print(-1)
