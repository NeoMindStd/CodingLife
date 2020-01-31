n,k=map(int,input().split())
m,M=k,1
l=[list(input().split())for _ in range(n)]
for i in l:
    a,b=int(i[0]),i[1]
    if b=='SAFE':M=max(M,a)
    elif b=='BROKEN':m=min(m,a)
print(M+1,m-1)
