k,p,x=map(int,input().split())
v=200000000
for m in range(1,10001):v=min(v,m*x+k/m*p)
print('%.3f'%v)
