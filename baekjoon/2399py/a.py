n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    for j in range(n):s+=abs(l[i]-l[j])
print(s)
