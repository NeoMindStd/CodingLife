a,b=tuple(sorted(map(int, input().split())))
print(max(min(b/3,a), min(a,b)/2))
