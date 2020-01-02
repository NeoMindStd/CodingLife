n=int(input())
c=0
for a in range(1+n,100001):
    b=a-n
    if int(a**.5)**2==a and int(b**.5)**2==b:c+=1
print(c)
