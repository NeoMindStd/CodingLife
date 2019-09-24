import sys
n, m = map(int, sys.stdin.readline().split())
floor = [list(sys.stdin.readline()) for _ in range(n)]

cnts = [[0] * ((n-7)*(m-7)) for _ in range(2)]
for i in range(n-7):
    for j in range(m-7):
        for key, pair in {0:('B', 'W'), 1:('W', 'B')}.items():
            for row in range(i, i+8):
                for col in range(j, j+8):
                    if floor[row][col] != pair[((row-i)+(col-j))%2]:
                        cnts[key][i*(m-7)+j] += 1
print(min(min(cnts[0]), min(cnts[1])))
