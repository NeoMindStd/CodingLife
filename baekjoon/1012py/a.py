for _ in range(int(input())):
    m, n, k = tuple(map(int, input().split()))
    bae = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = tuple(map(int, input().split()))
        bae[x][y] = 1

    while(max(map(max, bae)) > 0):
        cnt = 0
        stack = list()
        for i in range(m):
            for j in range(n):
                if(bae[i][j] == 1):
                    cnt +=1
                    stack.append((i, j))
                    while(len(stack) > 0):
                        x, y = stack.pop()
                        if(x+1 < len(bae) and bae[x+1][y] == 1): stack.append((x+1, y))
                        if(y+1 < len(bae[x]) and bae[x][y+1] == 1): stack.append((x, y+1))
                        if(x > 0 and bae[x-1][y] == 1): stack.append((x-1, y))
                        if(y > 0 and bae[x][y-1] == 1): stack.append((x, y-1))
                        bae[x][y] = 0
                        continue
    print(cnt)
