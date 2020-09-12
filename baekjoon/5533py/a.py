n = int(input())
l = [[], [], []]

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(3): l[j].append(s[j])


for j in range(n):
    t = 0
    for i in range(3):
        if l[i].count(l[i][j]) == 1: t += l[i][j]
    print(t)
