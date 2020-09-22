while True:
    a, b, c, d = map(int, input().split())
    if a == 0: break
    r1 = min(c/a, d/b)
    r2 = min(c/b, d/a)
    r = int(min(max(r1, r2), 1) * 100)
    print(f'{r}%')
