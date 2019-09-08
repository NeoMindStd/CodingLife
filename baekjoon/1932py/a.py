n = int(input())

t = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(i+1 if i > 0 else 0):
        tmp[j] += max(t[i-1][j-1] if j > 0 else 0, t[i-1][j] if j < i else 0)
    t.append(tmp)

print(max(t[n-1]))
