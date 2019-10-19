n = int(input())
a = list(map(int, input().split()))
m = [a[0]]
for i in range(1, n):
    m.append(max(m[i-1]+a[i], a[i]))
print(max(m))
