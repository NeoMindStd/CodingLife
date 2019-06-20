for T in range(int(input())):
    N = int(input())
    wall_scores = list(map(int, input()))
    parts_sum = [0 for i in range(N+1)]
    paintable = (N+1)//2
    for i in range(1, N+1):
        parts_sum[i] += parts_sum[i-1] + wall_scores[i-1]
    value = list()
    for i in range(paintable, N+1):
        value.append(parts_sum[i] - parts_sum[i-paintable])

    print("Case #"+str(T+1)+":", max(value))
