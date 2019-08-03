x, y, w, h = tuple(map(int, input().split()))
print(min(min(max(x, w) - min(x, w), x), min(max(y, h) - min(y, h), y)))
