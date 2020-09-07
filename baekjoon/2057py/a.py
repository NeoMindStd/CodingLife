n = int(input())

m = [1]

i = 1
while True:
    if m[-1]*i > n: break
    m.append(m[-1]*i)
    i += 1

f = False
def dfs(case):
    if sum(map(lambda i:m[i], case)) == n:
        global f
        f = True
        return
    for i in range(case[-1]+1, len(m)):
        if f:return
        dfs(case + [i])

i = 0
while i < len(m) and not f:
    dfs([i])
    i += 1

print('YES' if f else 'NO')
