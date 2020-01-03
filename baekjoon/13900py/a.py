n=int(input())
l=list(map(int,input().split()))
s=0
r=0
for i in range(n-1,0,-1):
    s+=l[i]
    r+=s*l[i-1]
print(r)
