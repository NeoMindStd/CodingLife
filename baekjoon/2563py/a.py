import sys
layer = [[0]*100 for _ in range(100)]
for _ in range(int(sys.stdin.readline())):
    r, c = map(int, sys.stdin.readline().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            layer[i][j] = 1
s = 0
for row in layer:
    s += sum(row)
print(s)
