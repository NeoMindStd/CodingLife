import sys

r = 1
for _ in range(int(sys.stdin.readline())):
    r += int(sys.stdin.readline()) - 1
print(r)
