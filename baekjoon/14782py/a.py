s,n=0,int(input())
for i in range(1,int(n**.5)+1):
    if n%i==0:
        s+=i
        if i*i!=n:s+=n//i
print(s)
