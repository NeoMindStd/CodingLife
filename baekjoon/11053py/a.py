n = int(input())
a = [0]+list(map(int, input().split()))
d = [0]*(n+1)
for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j])
    d[i] += 1
print(max(d))
