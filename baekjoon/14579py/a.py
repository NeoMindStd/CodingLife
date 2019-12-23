a,b=map(int,input().split())
r=1
for i in range(a,b+1):
    s=i*(i+1)//2
    r*=s
    r%=14579
print(r)
