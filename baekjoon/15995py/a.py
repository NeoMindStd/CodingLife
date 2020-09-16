a, m = map(int, input().split())
i = 1
while True:
    if (1 + i * m) / a == (1 + i * m) // a:
        print((1 + i * m) // a)
        break
    i += 1
