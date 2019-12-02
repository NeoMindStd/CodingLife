a,b,n,w=map(int,input().split())
if a==b:
    if a*n==w and n==2:print(1,1)
    else:print(-1)
else:
    y=(a*n-w)/(a-b)
    if y!=int(y):
       print(-1)
       exit(0)
    y=int(y)
    x=n-y
    if min(x,y) < 1:print(-1)
    else: print(x,y)
