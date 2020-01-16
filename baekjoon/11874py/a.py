l,d,x=(int(input())for _ in range(3))
n=m=0
for i in range(d-l+1):
    if n==0 and sum(map(int,str(l+i)))==x:n=l+i
    if m==0 and sum(map(int,str(d-i)))==x:m=d-i
    if n!=0!=m:break
print(n,m,sep='\n')
