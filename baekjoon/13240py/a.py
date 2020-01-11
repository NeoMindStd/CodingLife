n,m=map(int,input().split())
l=[['*'if (i+j)%2==0 else'.'for j in range(m)]for i in range(n)]
r=''
for row in l:r+=''.join(row)+'\n'
print(r)
