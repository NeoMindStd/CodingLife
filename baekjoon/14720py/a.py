n=int(input())
l=list(map(int,input().split()))
s=r=0
for i in l:
    if i==s:
        r+=1
        s=(s+1)%3
print(r)
