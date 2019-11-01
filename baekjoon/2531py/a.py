from sys import stdin

n,d,k,c=map(int,stdin.readline().split())
a=[int(stdin.readline()) for _ in range(n)]

z,m,r={i:0 for i in range(1,d+1)},0,set()
# 일단 먹고 뱉는식으로 생각
for i in range(k):
    if z[a[i]] == 0:
        m += 1
    z[a[i]]+=1
j = 1
while a[-j] == c:
    j-=1
    if z[c] == 0:
        m += 1
    z[c] += 1
if a[k%n] == c:
    if z[c] == 0:
        m += 1
    z[c] += 1

pl,pr=0,
for i in range(1,n+1):
    j = 1
    while a[i-j] == c:
        j-=1
    for idx in range(pl, i-j):
        z[a[idx]]-=1
        if  z[a[idx]] < 1:
            m-=1
    pl,j=i-j,0
    while a[(i+k+j)%n] == c:
        j+=1
    for idx in range(pr, i-j):
        if  z[a[idx]] < 1:
            m+=1
        z[a[idx]]+=1
    pr=(i+k+j)%n
    r.add(m)
print(max(m))
