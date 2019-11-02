apb,amb=map(int,input().split())
a=(apb+amb)//2
b=apb-a
if b>=0 and a<=1000 and a+b==apb and a-b==amb: print(*sorted([a,b],reverse=True))
else: print(-1)
