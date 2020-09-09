s = input()
n = len(s)

for i in range(int(n**.5),0,-1):
    if n % i == 0:
        r = i
        break

c = n//r

l = [['' for _ in range(c)] for _ in range(r)]

for j in range(c):
    for i in range(r):
        l[i][j] = s[r*j+i]

for row in l: print(*row, sep='', end='')
