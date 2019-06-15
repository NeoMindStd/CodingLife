a, b, c = input().split()

l = list(map(int, [a,b,c]))
l.remove(max(l))
print(max(l))
