n, k = tuple(map(int, input().split()))
money = list()

for _ in range(n):
    money.append(int(input()))


money.sort(reverse=True)

cnt = 0
for m in money:
    if(m <= k):
       cnt += k//m
       k %= m
       
print(cnt)
