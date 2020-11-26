for T in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0
    for b in range(2, n):
        for a in range(1, b):
            if (a**2 + b**2 + m) / (a*b) == (a**2 + b**2 + m) // (a*b):
                cnt += 1
    print(cnt)
