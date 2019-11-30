n,s=int(input()),set()
for i in range(1,int(n**.5)+1):
    if n%i==0:s.add(i);s.add(n//i)
print(sum(s)*5-24)
