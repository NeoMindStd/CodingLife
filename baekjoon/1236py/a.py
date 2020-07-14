n,m=map(int,input().split())
row,col=[False]*n,[False]*m
for i in range(n):
    s=input()
    for j in range(m):
        if s[j] == 'X':row[i]=col[j]=True
print(max(len(list(filter(lambda x:not x, row))),len(list(filter(lambda x:not x, col)))))
