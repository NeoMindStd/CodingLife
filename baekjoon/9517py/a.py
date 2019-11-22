k,n=int(input())-1,int(input())
l=[input().split() for _ in range(n)]
l=list(map(lambda x: (int(x[0]),x[1]),l))
s=0
for i in range(n):
    s+=l[i][0]
    if s>=210:break
    if l[i][1]=='T':k=(k+1)%8
print(k+1)
