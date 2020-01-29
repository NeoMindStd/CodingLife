n=int(input())
l=input().split()
for i in range(n):l[i]=i+1 if l[i]=='mumble'else int(l[i])
print('makes sense' if sum(l)==n*(n+1)//2 else'something is fishy')
