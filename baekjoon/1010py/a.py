cases = [[0]*31 for _ in range(31)]
cases[0][0] = 1

for i in range(1, 31):
    for j in range(0, i+1):
        cases[i][j] = (cases[i-1][j-1] if j > 0 else 0) + cases[i-1][j]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(cases[m][n])
