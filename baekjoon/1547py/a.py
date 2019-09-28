import sys

cups = [0]*4
cups[1] = 1

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    cups[a], cups[b] = cups[b], cups[a]

for i in range(1, 4):
    if cups[i] == 1:
        print(i)
        break
    if i == 3:
        print(-1)
