a, b = input(), input()

d = {}
for i in range(max(len(a), len(b))):
    if i < len(a):
        try: d[a[i]] += 1
        except: d[a[i]] = 1
    if i < len(b):
        try: d[b[i]] -= 1
        except: d[b[i]] = -1

print(sum(map(lambda x:abs(x), d.values())))
