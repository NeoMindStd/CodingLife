n, m = map(int, input().split())

for i in range(n): print(*[j+i*m for j in range(1, m+1)])
