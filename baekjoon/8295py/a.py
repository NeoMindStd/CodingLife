n,m,p=map(int,input().split())
r=0
for i in range(n):
    for j in range(m):
        if (i+j+2)*2>=p:r+=(n-i)*(m-j)
print(r)
