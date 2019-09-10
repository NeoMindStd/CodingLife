h, m = map(int, input().split())
tm = 60 * (h+24) + m - 45
print((tm // 60)%24, tm % 60)
