p,k=map(int,input().split())
f='GOOD'
for i in range(2,min(int(p**.5)+1,k)):
    if p%i==0:
        f=f'BAD {i}'
print(f)
