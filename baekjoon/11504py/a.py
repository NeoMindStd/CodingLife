for T in range(int(input())):
    n, m = map(int, input().split())
    x, y = int(''.join(input().split())), int(''.join(input().split()))
    board = input().split()
    
    cnt = 0
    acc = ''.join(board[:m])
    if x <= int(acc) <= y: cnt += 1
    for i in range(n - 1):
        acc = acc[1:] + board[(m + i) % n]
        if x <= int(acc) <= y: cnt += 1

    print(cnt)
