n, m = map(int, input().split())
a = [0]*m
c = [0]*m
g = [0]*m
t = [0]*m

for _ in range(n):
    dna = input()
    for i in range(len(dna)):
        if dna[i] == 'A': a[i] += 1
        elif dna[i] == 'C': c[i] += 1
        elif dna[i] == 'G': g[i] += 1
        else: t[i] += 1

hd = 0
for i in range(m):
    if a[i] >= c[i] and a[i] >= g[i] and a[i] >= t[i]:
        print('A', end="")
        hd += a[i]
    elif c[i] >= a[i] and c[i] >= g[i] and c[i] >= t[i]:
        print('C', end="")
        hd += c[i]
    elif g[i] >= a[i] and g[i] >= c[i] and g[i] >= t[i]:
        print('G', end="")
        hd += g[i]
    else:
        print('T', end="")
        hd += t[i]
print()

print(n*m-hd)
