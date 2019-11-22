n,T=map(int,input().split())
l=list(map(int,input().split()))
s=i=0
while i<n:
    s+=l[i]
    if s>T:break
    i+=1
print(i)
