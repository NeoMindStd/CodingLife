l=[[(i,j)for j in range(1,100)]for i in range(1,100)]
i=j=c=r=0
n=int(input())
while True:
    i=r
    for j in range(r+1):
        c+=1
        if c==n:break
        i-=1
    if c==n:break
    r+=1
print(*l[i][j])
