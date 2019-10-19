for _ in range(int(input())):
    s = int(input())
    opt = [tuple(map(int, input().split())) for _ in range(int(input()))]
    v = sum(map(lambda t: t[0]*t[1], opt))
    print(s+v)
