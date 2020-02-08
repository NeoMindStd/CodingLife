a,d,k=map(int,input().split())
n=(k-a)//d
print(n+1 if n>-1 and n*d+a==k else'X')
