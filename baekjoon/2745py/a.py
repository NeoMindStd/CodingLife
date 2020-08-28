n, b = input().split()
b = int(b)

d = {(str(i) if i < 10 else chr(55 + i)):i for i in range(36)}

s, t = 0, 1
for i in range(1,len(n)+1):
    s += d[n[-i]] * t
    t *= b
print(s)
