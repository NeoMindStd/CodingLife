n, k = map(int, input().split())

a = [list(map(int, input().split(','))),[]]

for i in range(k):
    a[(i+1)%2].clear()
    for j in range(n-i-1): a[(i+1)%2].append(a[i%2][j+1]-a[i%2][j])
    
print(*a[k%2], sep=',')
