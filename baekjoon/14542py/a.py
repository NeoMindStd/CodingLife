t=1
while True:
    n=int(input())
    if n==0:break
    l=[list(map(int,input().split()))for _ in range(n)]
    s=l[0][0]
    if n>1:s+=sum(l[-1])
    for i in range(1,n-1):s+=l[i][0]+l[i][-1]
    print(f'Case #{t}:{s}')
    t+=1
