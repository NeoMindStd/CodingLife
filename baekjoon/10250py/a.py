for T in range(int(input())):
    h, w, n = tuple(map(int, input().split()))
    count = 0
    for j in range(1, w+1):
        for i in range(1, h+1):
            count += 1
            if(count==n):
                break
        if(count==n):
            break
    print(i*100+j)
