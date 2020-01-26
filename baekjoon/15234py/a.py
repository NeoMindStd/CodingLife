n,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]+l[j]==k:s+=1
print(s)
