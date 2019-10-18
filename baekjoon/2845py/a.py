l, p = map(int, input().split())
print(*list(map(lambda x: x-l*p, list(map(int, input().split())))))
