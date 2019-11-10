n,k=map(int,input().split())
c=0
for i in range(1, n//2+1):
    if n%i==0:
        c+=1
        if c==k:break
if c==k:
    print(i)
elif c+1==k:
    print(n)
else:
    print(0)
