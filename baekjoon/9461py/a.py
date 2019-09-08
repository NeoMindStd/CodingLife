cnt = [1, 1, 1, 2, 2]

for i in range(5, 100):
    cnt.append(cnt[i-5]+cnt[i-1])
    
for _ in range(int(input())):
    n = int(input())
    print(cnt[n-1])
    pass
