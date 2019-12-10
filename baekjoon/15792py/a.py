a,b=map(int,input().split())
r=f"{a//b}."
a%=b
for i in range(1000):
    a*=10
    r+=str(a//b)
    a%=b
    if a==0:break
print(r)
