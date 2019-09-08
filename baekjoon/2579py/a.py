n = int(input())

t = [0]+[int(input()) for _ in range(n)]
d = [0]
for i in range(1, n+1):
    d.append(max(t[i-1] + t[i] + (d[i-3] if i > 2 else 0),\
                 t[i] + (d[i-2] if i > 1 else 0)))

print(d[n])


