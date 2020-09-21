n = int(input())
answer = 0

def bt(n, i, placable):
    print('================')
    print(i)
    for row in placable: print(row)
    print('================')
    if i >= n*n: return 1
    
    tmp = []
    if placable[i // n][i % n]:
        global answer
        answer += 1
        
        for row in placable: tmp.append(row.copy())
        for j in range(n): tmp[i // n][j] = tmp[j][i % n] = False
        j = 1
        while 0 <= i // n - j < n and 0 <= i % n - j < n:
            tmp[i // n - j][i % n - j] = False
            j += 1
        j = 1
        while 0 <= i // n + j < n and 0 <= i % n - j < n:
            tmp[i // n + j][i % n - j] = False
            j += 1
        j = 1
        while 0 <= i // n - j < n and 0 <= i % n + j < n:
            tmp[i // n - j][i % n + j] = False
            j += 1
        j = 1
        while 0 <= i // n + j < n and 0 <= i % n + j < n:
            tmp[i // n + j][i % n + j] = False
            j += 1
        
    i += 1
    while i < n*n and not placable[i // n][i % n]: i += 1
    if not tmp:  bt(n, i, tmp)
    bt(n, i, placable)

bt(n, 0, [[True] * n for _ in range(n)])
print(answer)
