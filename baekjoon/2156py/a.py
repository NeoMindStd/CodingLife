import sys

n = int(sys.stdin.readline())
wine = [0]+[int(sys.stdin.readline()) for _ in range(n)]

d = [0, wine[1], wine[1]+wine[2] if n > 1 else 0]
for i in range(3, n+1):
    d.append(max(d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i], d[i-1]))
print(d[n])
