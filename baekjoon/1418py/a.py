n, k = int(input()), int(input())

c = 1
for i in range(2, n+1):
    l = []
    j, tmp = 2, i
    while j*j <= tmp:
        if tmp % j == 0:
            tmp //= j
            l+=[j]
        else: j+= 1
    l.append(tmp)
    if max(l) <= k: c+= 1
print(c)
