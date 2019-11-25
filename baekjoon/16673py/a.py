c,k,p=map(int,input().split())
s=0
for i in range(1,c+1):s+=k*i+p*i**2
print(s)
