a = list(map(int, input().split()))
for i in range(5):
    a[i] **= 2
print(sum(a)%10)
