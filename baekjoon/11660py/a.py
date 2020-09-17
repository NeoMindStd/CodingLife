import sys; read = sys.stdin.readline

n, m = map(int, read().split())
table = [list(map(int, read().split())) for _ in range(n)]

memoization = [[0]*n for _ in range(n)]
memoization[0][0] = table[0][0]
for i in range(1, n):
    memoization[0][i] = memoization[0][i-1] + table[0][i]
    memoization[i][0] = memoization[i-1][0] + table[i][0]
    
for i in range(1, n):
    for j in range(1, n):
        memoization[i][j] = memoization[i-1][j] + memoization[i][j-1] +\
                            table[i][j] - memoization[i-1][j-1]

results = []
for i in range(m):
    x1, y1, x2, y2 = map(lambda x:int(x)-1, read().split())
    answer = memoization[x2][y2]
    if y1>0:
        answer -= memoization[x2][y1-1]
        if x1>0:
            answer -= memoization[x1-1][y2]
            answer += memoization[x1-1][y1-1]
    elif x1>0: answer -= memoization[x1-1][y2]
    results.append(answer)
print('\n'.join(map(str, results)))
