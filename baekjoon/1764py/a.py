import sys

n, m = map(int, sys.stdin.readline().split())
d = set()
b = set()
mans = []

for _ in range(n):
    mans.append(sys.stdin.readline())
    d.add(mans[-1])
    
for _ in range(m):
    mans.append(sys.stdin.readline())
    b.add(mans[-1])


dbj = []
mans = list(set(mans))
for man in mans:
    if man in d and man in b:
        dbj.append(man)
dbj.sort()

print(len(dbj))
print("".join(map(str, dbj)))
