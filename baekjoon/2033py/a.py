n = list(map(int, input()))

for i in range(len(n)-1, 0, -1):
    if n[i] > 4:
        n[i-1] += 1
    n[i] = 0

print(''.join(map(str,n)))
