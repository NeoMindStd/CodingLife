n,a,b=map(int,input().split())
l=[list(map(int,input().split()))for _ in range(n)]
a-=1
b-=1

f=l[a][b]==max(l[a])
for i in range(n):f &= l[i][b]<=l[a][b]
print('HAPPY'if f else'ANGRY')
